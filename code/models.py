import numpy as np

class ColaborativeFiltering:

    """
    the model class is about an implementation of HybridSVD which is such its name a collaborative 
    filtering based method developed in this research paper: https://arxiv.org/pdf/1802.06398.pdf
    Find more infos in markdown file wher i explain main ideas of the method
    """
    pass 

class TemporalClustering:
    def __init__(self, *args, **kwargs):
        
        if type(args) is not np.ndarray:
            raise Value
        self.X = args 
        self.sample_size , self.T = self.X.shape

    def raw_data(self,x=None, y=None, lp=2):
        return np.exp(np.log(np.sum(np.abs(np.power(x-y, lp))))/lp)

    def dynamic_time_warping(self):

        pass 

    def autocorrelation(self):
        
        pass 

    def spectral_domain(self):
        pass

    def xtream_value(self):
        pass 

    def model_based_ts(self):
        pass 

    def forecast_density(self):
        pass 

  













