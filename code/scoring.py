from tools import *
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class Naive:
    def __init__(self, file, grid_size):
        self.file = file 
        self.grid_size = grid_size 
        self.load_grid()
        self.data = None 

    def load_grid(self):
        grid = IterableBoundary()
        grid.grid_size = self.grid_size 
        self.grid = grid 

    @staticmethod 
    def __tuple__(x):
        return (x[0], x[1])
    
    def get_label(self, coor):
        point = Point(coor=coor)
        for boundary in self.grid:
            if point in boundary:
                return boundary.label
        return "boundary point"

    def fit(self):
        mms = MinMaxScaler()
        data = pd.read_table(self.file, sep=",", index_col=[0])
        taxi_id = data.iloc[0].id
        data.position_lon = mms.fit_transform(data.position_lon.values.reshape(-1, 1))
        data.position_lat = mms.fit_transform(data.position_lat.values.reshape(-1, 1))
        data["coor"] = data[["position_lon", "position_lat"]].apply(__tuple__, axis=1)
        data = data.drop(["position_lon", "position_lat", "time_stamp"], axis=1)
        data["label"] = data.coor.apply(lambda x: self.get_label(x))
        data = data.drop("coor", axis=1)
        data = data.groupby("label")["id"].count().reset_index()
        data = data.rename(columns={"label": "labelID", "id": "Rating"})
        data["taxiID"] = [taxi_id] * len(data)
        data = data[["taxiID", "labelID", "Rating"]]
        self.data = data 
        return "processing -- successed"

  










        


