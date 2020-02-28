
from sklearn.preprocessing import MinMaxScaler
from score import Naive 
import pandas as pd
import random 
import os 
import csv 


class Processing:

    """
    attributes
    ----------
    methods
    -------
    """

    def __init__(self, target=None, random=False, batch_size=1, full=False):
        self._FILES_REPO_PATH = "/Users/elhadjigagnysylla/Desktop/Machine_learning/datasets/taxi/data/taxi_log_2008_by_id"
        self._BATCH_FILE_OUTPUT_PATH = "/Users/elhadjigagnysylla/Desktop/Machine_learning/datasets/taxi/data/T drive processed/"
        if not target:
            if full:
                raise ValueError("the given value for full parameter is deprecated -- memory restriction")
            if not random:
                raise ValueError("if not target, random must be automatically set to True")
            self.target = target
        self._target = target 
        self.batch_size = batch_size
        self.full = full 
        self.random = random and self.target is None
        self.tracking_files = [] # set it only for random option 
        self._STATIC_COLUMN_NAMES = ["id", "time_stamp", "position_lon", "position_lat"]

    def __str__(self):
        return "infos -- {}".format(self.__dict__)
        # a simple way to do it ... dict keys must be more explicit 
        # return self.__dict__

    def _random_generating(self): # make this function recursive 
        whl = True
        while whl:
            for _ in range(self. batch_size):
                file = os.path.join(self._FILES_REPO_PATH,random.choice(os.listdir(self._FILES_REPO_PATH)))
                self.tracking_files.append(file)
            whl = len(set(self.tracking_files)) != self.batch_size
    
    def fit_batch(self, *args, **kwargs):
        if self.target:
            return 
        # get (batch_size) random files and save their paths into self.tracking_files list 
        self._random_generating()

    def get_csv(self, *args, **kwargs):
        if self.target:
            return self.target 
        else:
            return self.tracking_files


class ProcessingForRS(Processing):

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
        

class ProcessingForClustering(Processing):
    def __init__(self, target=None, random=False, batch_size=1, full=False, others=None):
        super().__init__(target=None, random=False, batch_size=1, full=False)
        self.others = others 


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

if __name__ == "__main__":
    main()
