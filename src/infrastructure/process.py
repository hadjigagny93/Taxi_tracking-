
from sklearn.preprocessing import MinMaxScaler
from .score import Naive 
import pandas as pd

import os 
import csv 
from .generate import GenerateDataset


class ProcessingForRS(GenerateDataset):

    def __init__(self, target=None, random=False, batch_size=1, full=False, rating="Naive", grid_size=10):
        super().__init__(target=target, random=random, batch_size=batch_size, full=full)
        self.rating = rating
        self.grid_size = grid_size 
    
    @staticmethod
    def is_columns_name_or_not(file):
        with open(file, "r") as f:
            x = f.readline()
        return x.rstrip().split(",")[0].isnumeric()

    def process(self):
        w = {False: self.target, True: self.tracking_files}
        files = w[self.random is True]
        dataframes = []
        mms = MinMaxScaler()
        scorer = Naive(grid_size=self.grid_size)
        for file in files:  
            if self.is_columns_name_or_not(file):
                names = self._STATIC_COLUMN_NAMES
                data = pd.read_table(file, sep=",", index_col=[0], names=names).reset_index()
            else:
                data = pd.read_table(file, sep=",", index_col=[0])
            taxi_id = data.iloc[0].id
            data.position_lon = mms.fit_transform(data.position_lon.values.reshape(-1, 1))
            data.position_lat = mms.fit_transform(data.position_lat.values.reshape(-1, 1))
            data["coor"] = data[["position_lon", "position_lat"]].apply(scorer.__tuple__, axis=1)
            data = data.drop(["position_lon", "position_lat", "time_stamp"], axis=1)
            data["label"] = data.coor.apply(lambda x: scorer.get_label(x))
            data = data.drop("coor", axis=1)
            data = data.groupby("label")["id"].count().reset_index()
            data = data.rename(columns={"label": "labelID", "id": "Rating"})
            data["taxiID"] = [taxi_id] * len(data)
            data = data[["taxiID", "labelID", "Rating"]]
            dataframes.append(data)
        return pd.concat(dataframes ,ignore_index=True)
        


# main function --- call ProcessingForRS class 
# generate a random file for testing some  
# reccommander system algorithms 

def generate_file_for_RS_models():
    pr = ProcessingForRS(random=True, batch_size=5)
    pr.fit_batch()
    rating_taxi = pr.process()
    rating_taxi.to_csv(os.path.join(pr._BATCH_FILE_OUTPUT_PATH,"test_data.csv"))

def main():
    generate_file_for_RS_models()

#if __name__ == "__main__":
#    main()
