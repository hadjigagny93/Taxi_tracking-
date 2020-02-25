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

    def __init__(self, file):
        self.file = file
        self.load_info()

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
    def lines(self):
        f, *_ = args 
        self.lines  = f.readlines()

    def user(self):
        self.user, *infos = self.lines[0].split(",")

    def records(self):
        self.records = len(self.lines)

    def distance(self):
        lines = self.lines 
        size_x = self.records 
        end_d = [(elt.split(",")[3], elt.split(",")[2]) for elt in lines[1:]]
        start_d = [(elt.split(",")[3], elt.split(",")[2]) for elt in lines[:size_x-1]]
        self.distance = sum([self.get_granular_distance(s[0], s[1]) for s in zip(start_d, end_d)])

    def time(self):
        lines = self.lines 
        size_x = self.records
        end = [elt.split(",")[1] for elt in lines[1:]]
        start = [elt.split(",")[1] for elt in lines[:size_x-1]]
        self.time = self.sumtime(delta=[self.get_granular_duration(s[0], s[1]) for s in zip(start, end)])

    def speed(self):
        self.speed =  10000 * self.distance / self.time.seconds

    def load_info(self):
        try:
            self.lines()
            self.user()
            self.records()
            self.distance 
            self.time()
            self.speed()
        except:
            raise ValueError("Class import error")

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

    @staticmethod
    def hour_detection(timestamp=None):
        return 
    
    @staticmethod
    def day_detection(timestamp=None):
        return 
    
    @staticmethod
    def detect_user_ride(self, *args, **kwargs):
        return