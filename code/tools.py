import geopy.distance as ds 
import numpy as np 
import datetime 

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








        


    
  


    

    

    








     