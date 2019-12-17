    
import geopy.distance as ds 
import datetime 
import numpy as np 

(lon_inf, lon_sup, lat_inf, lat_sup) = (0,0,0,0) # TODO 

class GeoDataProcess:

    def __init__(self, city_limits, *args, **kwargs):

        self.mesh = None 
        if city_limits:
            self.beiijing_limits = city_limits 
        else:
            self.beiijing_limits = (lon_inf, lon_sup, lat_inf, lat_sup)
    
        
        self.lon = np.linspace(lon_inf, lon_sup, size + 1)
        self.lat = np.linspace(lat_inf, lat_sup, size + 1)
    

    def get_granular_distance(self, lon_start=None, lat_start=None, lon_end=None, lat_end=None):
    
        position_start, position_end = (lon_start, lat_start), (lon_end, lat_end)
        return ds.vincenty(position_start, position_end).km 
      
    def get_granular_duration(self, time_start=None, time_end=None):

        time_start = datetime.datetime.strptime(time_start,'%Y-%m-%d %H:%M:%S.%f')
        time_end   = datetime.datetime.strptime(time_end,'%Y-%m-%d %H:%M:%S.%f')
        return time_end - time_start
    
    def get_granular_speed(self, lon_start=None, lat_start=None, lon_end=None, lat_end=None, time_start=None, time_end=None):

        return self.get_granular_distance(lon_start, lat_start, lon_end, lat_end, time_start, time_end)/ self.get_granular_duration(time_start, time_end)

    def mesh_intersect(self,i=0,size=50):

        lon = self.lon
        lat = self.lat
        return ((lat[i//size], lon[i%size]), (lat[i//size] ,lon[i%size +1]), (lat[i//size +1],lon[i%size]), (lat[i//size +1],lon[i%size + 1]))

    def update_mesh(self, size=50):

        """
        update mesh class attribute as a dictionnary containing a tuple of 
        4 tuples (lat_k, lon_k) for k in [0, 1]

        ex:
        ---
        ((lat_0, lon_O), (lat_0, lon_1),(lat_1, lon_O),(lat_1, lon_1)) as key 
        j: as value with j in range(size**2)
        """
        if self.mesh:
            return
        else:

            self.mesh =  {self.mesh_intersect(i): i for i in range(size**2)}

    def match_position_grid(self, lat, lon):

        if not self.mesh:
            self.update_mesh()

        # get dict key by performing two simultanaite quicksort research 
        # over lat & lon attributes 

        x = list(1 * (self.lat <= lat)).index(0)
        y = list(1 * (self.lon <= lon)).index(0)
 
        _key_ = (
            (self.lat[x-1], self.lon[y-1]),
            (self.lat[x-1], self.lon[y]),
            (self.lat[x], self.lon[y-1]),
            (self.lat[x], self.lon[y]))

        return self.mesh[_key_]

        


    






















        


    
  


    

    

    








        






 



        return 


    def grid_search(self, lon , lat):

        return 

    