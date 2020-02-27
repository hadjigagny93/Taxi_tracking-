from geopy import distance as ds 
import datetime

class TargetInfo:
    
    """
    this class is created to return some infos about a trajectory data informations 
    recoreded in a given file. here is a description of all attributes and methods 
    developed in the class

    attributes:
    -----------
    methods:
    --------
    """ 

    def __init__(self, file):
        self.file = file
        self._load_info()

    def __str__(self):
        return "user  --- {} , distance --- {}, speed --- {}, time --- {}, records --- {}".format(self.user, self.distance, self.speed, self.time, self.records)

    def infile(foo):
        def wrapper(self):
            try:
                with open(self.file) as f:
                    foo(self, f)
            except OSError:
                print("file not found")
        return wrapper
    """
    @infile
    def update_instance(self, *args, **kwargs): # optimize and factorize
        f, *_ = args 
        lines  = f.readlines()
        self.user, *infos = lines[0].split(",")
        size_x = self.records_all = len(lines)
        end = [elt.split(",")[1] for elt in lines[1:]]
        start = [elt.split(",")[1] for elt in lines[:size_x-1]]
        self.time_all = self.sumtime(delta=[self.get_granular_duration(s[0], s[1]) for s in zip(start, end)])
        end_d = [(elt.split(",")[3], elt.split(",")[2]) for elt in lines[1:]]
        start_d = [(elt.split(",")[3], elt.split(",")[2]) for elt in lines[:size_x-1]]
        self.distance_all = sum([self.get_granular_distance(s[0], s[1]) for s in zip(start_d, end_d)])
        self.velocity_all =  10000 * self.distance_all / self.time_all.seconds
    """
    @infile
    def _lines(self, *args, **kwargs):
        print("debug lines")
        f, *_ = args 
        self.lines  = f.readlines()
    
    
    def _user(self):
        print("debug user")
        self.user, *infos = self.lines[0].split(",")
    
    def _records(self):
        print("debug records")
        self.records = len(self.lines)
    
    def _distance(self):
        print("debug distance")
        lines = self.lines 
        lines = lines[1:]
        size_x = self.records 
        end_d = [(elt.split(",")[4].rstrip(), elt.split(",")[3]) for elt in lines[1:]]
        start_d = [(elt.split(",")[4].rstrip(), elt.split(",")[3]) for elt in lines[:size_x-1]]
        #print(end_d[0])
        #print(start_d[0])
        #print("list of distance -- {}".format(sum([self.get_granular_distance(s[0], s[1]) for s in zip(start_d, end_d)])))
        #return 
        self.distance = sum([self.get_granular_distance(s[0], s[1]) for s in zip(start_d, end_d)])
    
    def _time(self):
        print("debug time")
        lines = self.lines 
        lines = lines[1:]
        size_x = self.records
        end = [elt.split(",")[2] for elt in lines[1:]]
        start = [elt.split(",")[2] for elt in lines[:size_x-1]]
        #print(end[0])
        #print(start[0])
        #return 
        self.time = self.sumtime(delta=[self.get_granular_duration(s[0], s[1]) for s in zip(start, end)])

    def _speed(self):
        print("debug speed")
        self.speed =  10000 * self.distance / self.time.seconds

    def _load_info(self):
        try:
            self._lines()
            self._user()
            self._records()
            self._distance()
            #print("distance -- {}".format(self.distance))
            self._time()
            self._speed()
        except:
            raise ValueError("Class import error")
    """
    @staticmethod 
    def __float__(x):
        return (float(x[0]), float(x[1]))
    """

    @staticmethod
    def get_granular_distance(position_start, position_end):
        position_start, position_end = (float(position_start[0]), float(position_start[1])), (float(position_end[0]), float(position_end[1]))
        #print("position start -- {}".format(position_start))
        #print("position end -- {}".format(position_end))
        #print("distance -- {}".format(ds.vincenty(position_start, position_end).km))
        #return 
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

    @staticmethod
    def hour_detection(timestamp=None):
        return 
    
    @staticmethod
    def day_detection(timestamp=None):
        return 
    
    @staticmethod
    def detect_user_ride(self, *args, **kwargs):
        return