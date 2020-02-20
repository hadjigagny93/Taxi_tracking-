"""
this module contains some maths functions for 
evaluating some movements characteristics 

"""
from tools import get_granular_distance, get_granular_duration, get_granular_speed
import os 

class FileTrajectoryAnalysis:
    """
    this class is created to return some infos about a trajectory data informations 
    recoreded in a given file. here is a description of all attributes and methods 
    developed in the class

    attributes:
    -----------
    methods:
    --------
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.user = None 
        self.records_all =  None 
        self.time_all = None 
        self.distance_all = None 
        self.velocity_all = None 
        self.d_time = None  
        self.d_distance = None 
        self.d_velocity = None 
        self.d_records = None 
        self.h_time = None 
        self.h_distance = None 
        self.h_velocity = None 
        self.h_records = None 

    def decor(foo):
        def wrapper(self):
            try:
                with open(self.path) as f:
                    foo(self, f)
            except OSError:
                print("file do not exist")
        return wrapper

    @decor
    def get_user(self, *args, **kwargs):
        f, *_ = args
        self.user, *infos = f.readline()

    @decor
    def get_records_all(self, *args, **kwargs):
        f, *_ = args 
        self.records_all = len(f.readlines())

    @decor
    def get_time_all(self):
        f, *_ = args 
        x = f.readlines()
        size_x = len(x)
        end = [elt.split(",")[1] for elt in x[1:]]
        start = [elt.split(",")[1] for elt in x[:size_x-1]]
        self.time_all = [get_granular_duration(s[0], s[1]) for s in zip(start, end)]

    @staticmethod
    def get_granular_distance(lon_start=None, lat_start=None, lon_end=None, lat_end=None):
        position_start, position_end = (lon_start, lat_start), (lon_end, lat_end)
        return ds.vincenty(position_start, position_end).km 

    @staticmethod 
    def get_granular_duration(time_start=None, time_end=None):
        time_start = datetime.datetime.strptime(time_start,'%Y-%m-%d %H:%M:%S.%f')
        time_end   = datetime.datetime.strptime(time_end,'%Y-%m-%d %H:%M:%S.%f')
        return time_end - time_start

    @staticmethod 
    def get_granular_speed(self, lon_start=None, lat_start=None, lon_end=None, lat_end=None, time_start=None, time_end=None):
        return self.get_granular_distance(lon_start, lat_start, lon_end, lat_end, time_start, time_end)/ self.get_granular_duration(time_start, time_end)

    def get_d_velocity(self):
        return 

    def get_d_records(self):
        return 

    def get_h_time(self):
        return 

    def get_h_distance(self):
        return 

    def get_h_velocity(self):
        return 

    def get_h_records(self):
        return 
    
    @staticmethod
    def hour_detection(timestamp=None):
        return 
    
    @staticmethod
    def day_detection(timestamp=None):
        return 
    
    @staticmethod
    def detect_user_ride(self, *args, **kwargs):
        return 
    





            


