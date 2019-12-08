"""
this module contains some maths functions for 
evaluating some movements characteristics 

"""
from tools import get_granular_distance, get_granular_duration, get_granular_speed




class TrajectoryAnalysis:

    def __init__(self, lon=None, lat=None, time=None, user=None):
        """
        lon: array of number 
        lat:
        time:
        """
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






            


