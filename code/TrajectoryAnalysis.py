import geopy.distance as ds 
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
        self.path = file_path
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
    def update_instance(self, *args, **kwargs): # optimi ze 
        f, *_ = args
        lines  = f.readlines()
        self.user, *infos = f.readline().split(",")
        self.records_all = len(lines)
        size_x = self.records_all
        end = [elt.split(",")[1] for elt in lines[1:]]
        start = [elt.split(",")[1] for elt in lines[:size_x-1]]
        self.time_all = self.sumtime(delta=[self.get_granular_duration(s[0], s[1]) for s in zip(start, end)])
        
        end_d = [(elt.split(",")[3], elt.split(",")[2]) for elt in lines[1:]]
        start_d = [(elt.split(",")[3], elt.split(",")[2]) for elt in lines[:size_x-1]]
        self.distance_all = sum([self.get_granular_distance(s[0], s[1]) for s in zip(start_d, end_d)])
        
        self.velocity_all =  10000 * self.distance_all / self.time_all.seconds
           
      

    @staticmethod
    def get_granular_distance(position_start, position_end):
        #position_start, position_end = (lon_start, lat_start), (lon_end, lat_end)
        return ds.vincenty(position_start, position_end).km 

    @staticmethod 
    def get_granular_duration(time_start=None, time_end=None):
        time_start = datetime.datetime.strptime(time_start,'%Y-%m-%d %H:%M:%S')
        time_end   = datetime.datetime.strptime(time_end,'%Y-%m-%d %H:%M:%S')
        return time_end - time_start

    @staticmethod 
    def get_granular_speed(self, lon_start=None, lat_start=None, lon_end=None, lat_end=None, time_start=None, time_end=None):
        return self.get_granular_distance(lon_start, lat_start, lon_end, lat_end, time_start, time_end)/ self.get_granular_duration(time_start, time_end)
    
    @staticmethod 
    def sumtime(delta):
        x = datetime.timedelta(seconds=0)
        for time in delta:
            x += time 
        return x

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
    """