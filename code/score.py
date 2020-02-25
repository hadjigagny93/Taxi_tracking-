from tools import *


class Naive:
    def __init__(self, grid_size):
        self.grid_size = grid_size 
        self.load_grid()

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

  











        


