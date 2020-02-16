"""
this module contains some maths functions for 
evaluating some movements characteristics 

"""
from tools import get_granular_distance, get_granular_duration, get_granular_speed
import os 

    """

    def __init__(self, lon=None, lat=None, time=None, user=None):
    
        # lon: array of number 
        # lat:
        # time:
    
        if len(lon) == len(lat) == len(time):
            time = [datetime.datetime.strptime(string_time,'%Y-%m-%d %H:%M:%S.%f') for string_time in time]
            self.lon, self.lat, self.time = lon, lat, time 
        else: 
            raise ValueError("Not matching dimeensions")

        self.size_trajectory = len(self.lon)
        self.user = user 
        self.duration = self.time[1:] - self.time[:len(self.time) - 1]
        self.distance = np.asarray([get_granular_distance(lon_0, lat_0, lon_1, lat_1) for lon_0, lat_0, lon_1, lat_1 in zip(self.lon[:len(self.lon) - 1], self.lat[:len(self.lat) - 1], self.lon[1:],self.lat[1:],)])
        self.speed = self.distance / self.duration 

    """



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

    @decor
    def get_distance_all(self):
        pass 


        






        return 

    def get_velocity_all(self):
        return 




    
    def get_d_time(self):
        return 

    def get_d_distance(self):
        return 

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


















    







    
    



    
    

    




def get_distance(self):
    return 

def get_time(self):
    return 

def get_speed(self):
    
    return 

def hour_detection(self, timestamp=None):
    return 

def day_detection(self, timestamp=None):
    return 


def detect_user_ride(self, *args, **kwargs):
    return 






            


