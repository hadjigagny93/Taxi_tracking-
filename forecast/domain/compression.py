

import numpy as np 

from dataclasses import dataclass 



@dataclass 
class FastStray:
    """A global class that implements faststray algorithms for reduction GPS data point in a given trajectory 
    For more information about the method, you can check the paper on https://arxiv.org/pdf/1608.07338.pdf
    
    
    attributes
    ----------
    alpha: size of the moving average filter 
    beta: size of the neighborhood to measure the correaltion coef
    gamma: size of the neighboorhood to perform the non maximum suppression

    methods:
    linear_correlation_based_coef: static method, evaluate the correlation between space and time informations 
    ksi_function: more larger is ksi the more information  we can extract  from the related point 
    """

    alpha: float
    beta: float 
    gamma: float 
    position: np.ndarray
    spatial_position: np.ndarray = position[:,0:2]
    temporal_position: np.ndarray = position[:, 2]

    filtering_spatial_position: np.ndarray
    filtering_temporal_position: np.ndarray 

    sample_size: int = position.shape[1]
    spatial_dim: tuple = (sample_size, 2)
    temporal_dim: tuple = (sample_size, 1)

    def moving_average_smooth_traject(self):
        #N, _ = self.position.shape
        new_spatial_position = np.zeros(self.spatial_dim)
        new_temporal_position = self.temporal_position
        for i in range(self.sample_size):
            j_index = alpha_index(i, alpha=self.alpha, beta=self.beta, sample_size=self.sample_size)
            new_spatial_position[i] = self.spatial_position[j_index,:].mean(axis=0)
        return new_spatial_position, new_temporal_position


    def update_filtering_position(self):
        self.filtering_spatial_position, self.filtering_temporal_position = self.moving_average_smooth_traject()

    @staticmethod 
    def hyperparams_index(idx, alpha, beta, sample_size):
        inf = max(0, idx - alpha)
        sup = min(idx + alpha, sample_size)
        return np.range(inf, sup + 1)

    @staticmethod
    def linear_correlation_based_coef(cls, aa, tt):
        cov = np.sum((aa - np.mean(aa))*(tt - np.mean(tt)))
        std_a = np.sqrt(np.sum(aa - np.mean(aa)**2))
        std_t = np.sqrt(np.sum(tt - np.mean(tt)**2))
        return  cov/ (std_a * std_t)
        
    @staticmethod
    def ksi_func(cls, pp, tt):
        ppx, ppy = pp.T
        rat_x = cls.linear_correlation_based_coef(ppx, tt) ** 2
        rat_y = cls.linear_correlation_based_coef(ppy, tt) ** 2
        return 1./ rat_x + 1./ rat_y 







def main():
    A = FastStray(alpha=0, beta=0, gamma=0, position= np.ones(3))
    print(A)
  


if __name__ == "__main__":
    main()
