
import datetime
import geopy.distance as ds 
import numpy as np 


class Point:
    """
    Abstract point class with x, y as natural attribute which 
    models cartesian coordinates

    attributes
    ----------
    x, y: cartesian coordinates 

    methods
    -------
    new_point: class method , return a new instance with specified coordinates 
    add: class instance method that perform translation transformation 
    """
    def __init__(self, coor):
        self.x , self.y = coor

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    @classmethod
    def new_point(cls, coor):
        return cls(coor=coor)
    
    def add(self, pas):
        coor = (self.x + pas[0], self.y + pas[1])
        return self.new_point(coor)
        
class Boundary:
    """
    Container object
    
    attributes
    ----------
    point0: up left point 
    point1: up right
    point2: down right 
    point3: down left 
    label: for labeling taxi position for the recommander system

    methods
    -------
    contains: magic method included for test if a given 
    point is or not inside the square defined by the four given just below 
    """
    geometry = "SQ"
    def __init__(self, point0=None, point1=None, point2=None, point3=None, label=None):
        self.point0 = point0
        self.point1 = point1 
        self.point2 = point2
        self.point3 = point3 
        self.label = label
        
    def __str__(self):
        return "{} --- {}, {}, {}, {}".format(self.label, self.point0, self.point1, self.point2, self.point3)
    
    def __contains__(self, point):
        x1 , y1 = self.point0.x, self.point0.y
        x2 , y2 = self.point1.x, self.point1.y
        x3 , y3 = self.point2.x, self.point2.y
        x4 , y4 = self.point3.x, self.point3.y
        return x1 < point.x < x3 and y4 < point.y < y2
    
    
class IterableBoundary:
    """
    >>>from .. import ItarableBoundary 
    >>>iterable_boundary = IterableBoundary()
    >>>iterable_boundary.grid_size = 4
    >>>for boundary in iterable_boundary:
    >>>print(boundary)
    0 --- (0.0, 0.25), (0.25, 0.25), (0.25, 0.0), (0.0, 0.0)
    1 --- (0.25, 0.25), (0.5, 0.25), (0.5, 0.0), (0.25, 0.0)
    2 --- (0.5, 0.25), (0.75, 0.25), (0.75, 0.0), (0.5, 0.0)
    3 --- (0.75, 0.25), (1.0, 0.25), (1.0, 0.0), (0.75, 0.0)
    4 --- (0.0, 0.5), (0.25, 0.5), (0.25, 0.25), (0.0, 0.25)
    5 --- (0.25, 0.5), (0.5, 0.5), (0.5, 0.25), (0.25, 0.25)
    6 --- (0.5, 0.5), (0.75, 0.5), (0.75, 0.25), (0.5, 0.25)
    7 --- (0.75, 0.5), (1.0, 0.5), (1.0, 0.25), (0.75, 0.25)
    8 --- (0.0, 0.75), (0.25, 0.75), (0.25, 0.5), (0.0, 0.5)
    9 --- (0.25, 0.75), (0.5, 0.75), (0.5, 0.5), (0.25, 0.5)
    10 --- (0.5, 0.75), (0.75, 0.75), (0.75, 0.5), (0.5, 0.5)
    11 --- (0.75, 0.75), (1.0, 0.75), (1.0, 0.5), (0.75, 0.5)
    12 --- (0.0, 1.0), (0.25, 1.0), (0.25, 0.75), (0.0, 0.75)
    13 --- (0.25, 1.0), (0.5, 1.0), (0.5, 0.75), (0.25, 0.75)
    14 --- (0.5, 1.0), (0.75, 1.0), (0.75, 0.75), (0.5, 0.75)
    15 --- (0.75, 1.0), (1.0, 1.0), (1.0, 0.75), (0.75, 0.75)
    """
    def __init__(self):
        self.F0 = Point((0,1))
        self.F1 = Point((1,1))
        self.F2 = Point((1,0))
        self.F3 = Point((0,0))

    def mesh(self):
        self.lon_mesh = np.linspace(self.F0.x, self.F1.x, self._grid_size + 1)
        self.lat_mesh = np.linspace(self.F2.y, self.F1.y, self._grid_size + 1)
    
    @property 
    def grid_size(self):
        return self._grid_size
    
    @grid_size.setter
    def grid_size(self, grid_size):
        if grid_size <= 0:
            raise ValueError("Can not be negative int")
        self._grid_size = grid_size 
        self.start = 0
        self.end = self._grid_size**2
        self.mesh()
            
    def __iter__(self):
        index = 0
        while index < self.end:
            current_boundary = self.get_current_boundary(index)
            yield current_boundary
            index += 1

    @staticmethod 
    def div(j, k):
        return j // k, j % k
    
    def get_current_boundary(self, i):
        y_idx, x_idx = self.div(i, self._grid_size)
        static_point = Point((self.lon_mesh[x_idx], self.lat_mesh[y_idx]))
        point0 = static_point.add((0,.25)) #point0 = Point((self.lon_mesh[x_idx], self.lat_mesh[y_idx+1]))
        point1 = static_point.add((.25,.25)) #point1 = Point((self.lon_mesh[x_idx+1], self.lat_mesh[y_idx+1]))
        point2 = static_point.add((.25,0)) #point2 = Point((self.lon_mesh[x_idx+1], self.lat_mesh[y_idx]))
        point3 = static_point.add((0,0)) #point3 = Point((self.lon_mesh[x_idx], self.lat_mesh[y_idx]))
        return Boundary(point0, point1, point2, point3, i)

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