

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
    position: lon, lat, timestamp data dim = (n_samples, 3)
    spatial_position: lon, lat dim = (n_samples, 2)
    temporal_position: timestamp dim = (n_samples, )
    filtering_spatial_data: moving average on spatial_position
    filtering_temporal_position: moving average on temporal_position data 

    methods:
    --------
    linear_correlation_based_coef: static method, evaluate the correlation between space and time informations 
    ksi_function: more larger is ksi the more information we can extract from the related point 
    moving_average_smooth_trajectory: moving average 
    update_filtering_position: return of MA methods 
    get_params_idx: return intervall which one apply MA algorithm on -- this allows specifying windows for inference
    """
    alpha: float
    beta: float 
    gamma: float 
    position: np.ndarray
    spatial_position: np.ndarray = position[:,0:2]
    temporal_position: np.ndarray = position[:, 2]

    filtering_spatial_position: np.ndarray
    filtering_temporal_position: np.ndarray 

    simplified_spatial_position: np.ndarray 
    simplified_temporal_position: np.ndarray 


    coeff: list = []

    sample_size: int = position.shape[1]
    spatial_dim: tuple = (sample_size, 2)
    temporal_dim: tuple = (sample_size, 1)

    def moving_average_smooth_traject(self):
        new_spatial_position = np.zeros(self.spatial_dim)
        new_temporal_position = self.temporal_position
        for i in range(self.sample_size):
            j_index = self.get_params_idx(idx=i, param="alpha", value=self.alpha, sample_size=self.sample_size)
            new_spatial_position[i] = self.spatial_position[j_index,:].mean(axis=0)
        return new_spatial_position, new_temporal_position


    def update_filtering_position(self):
        # P1 -- filtering_spatial_position
        # S1 -- iltering_temporal_position
        self.filtering_spatial_position, self.filtering_temporal_position = self.moving_average_smooth_traject()

    def get_coeff_on_filtering_traject(self, idx):
        filtering_interval = self.get_params_idx(idx, "other", self.beta, self.sample_size)
        p_nu = self.filtering_spatial_data[filtering_interval,:]
        t_nu = self.filtering_temporal_position[filtering_interval]
        return self.ksi_func(p_nu, t_nu)

    def update_coeff(self):
        for i in range(self.sample_size):
            self.coeff.append(self.get_coeff_on_filtering_traject(i))


    def open_simplified_traject(self):
        self.simplified_spatial_position = self.filtering_spatial_position[0,:]
        self.simplified_temporal_position = self.filtering_temporal_position[0]

    def update_simplified_traject_local(self, idx):
        filtering_interval = self.get_params_idx(idx, "other", self.gamma, self.sample_size)
        filtering_coeff = self.coeff[filtering_interval]
        m_p = max(filtering_coeff)
        if self.coeff[idx] == m_p:
            # update simplified sptial data 
            self.simplified_spatial_position = np.vstack(
                self.simplified_spatial_position,
                self.filtering_spatial_position[i,:]
                )
            # update simplified temporal data 
            self.simplified_temporal_postion = np.append(
                self.simplified_temporal_position,
                self.filtering_temporal_position) 
    
    def update_simplified_trajectory_global(self):

        for i in range(self.sample_size):
            self.update_simplified_traject(i)
        #return self.simplified_spatial_position, self.simplified_temporal_postion

    def close_simplified_trajectory(self):

        # add last lon lat point 
        self.simplified_spatial_position = np.vstack(
            self.simplified_spatial_position,
            self.filtering_spatial_position[self.sample_size-1,:]
                )
        # add last timestamp
        self.simplified_temporal_postion = np.append(
            self.simplified_temporal_position,
            self.filtering_temporal_position[self.sample_size-1])

    def fit_model(self):
        self.update_filtering_position()
        self.update_coeff()
        self.open_simplified_traject()
        self.update_simplified_trajectory_global()
        self.close_simplified_trajectory()

    def predict(self):
        return self.simplified_spatial_position, self.simplified_temporal_position

    def reduction_probs(self):
        """
        the percentage of redudtion data in init trajectory
        """
        pass

    @staticmethod 
    def get_params_idx(idx, param, value, sample_size):
        map_dict = {
            "alpha": (max(0, idx - value), min(idx + value, sample_size) + 1),
            "other": (idx - value, idx + value + 1),
        }
        inf, sup = map_dict[param]
        return np.range(inf, sup)

    @staticmethod
    def linear_correlation_based_coef(aa, tt):
        cov = np.sum((aa - np.mean(aa))*(tt - np.mean(tt)))
        std_a = np.sqrt(np.sum(aa - np.mean(aa)**2))
        std_t = np.sqrt(np.sum(tt - np.mean(tt)**2))
        return  cov/ (std_a * std_t)
        

    def ksi_func(self, pp, tt):
        ppx, ppy = pp.T
        rat_x = self.linear_correlation_based_coef(ppx, tt) ** 2
        rat_y = self.linear_correlation_based_coef(ppy, tt) ** 2
        return 1./ rat_x + 1./ rat_y 

# ============= Unuseful static method methods 

    @staticmethod 
    def alpha_index(idx, alpha, sample_size):
        inf = max(0, idx - alpha)
        sup = min(idx + alpha, sample_size) + 1
        return  np.range(inf, sup)

    @staticmethod
    def beta_index(idx, beta, sample_size):
        inf = idx - beta
        sup = idx + beta + 1
        return np.range(inf, sup)

    @staticmethod 
    def gamma_index(idx, gamma, sample_size):
        inf = idx - gamma 
        sup = idx + gamma + 1 
        return np.range(inf, sup)
# ===================================================
def main():
    pass 

if __name__ == "__main__":
    main()