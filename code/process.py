import os 
import random 
import csv 

from scoring import Naive 
class Processing:
    """
    attributes
    ----------
    methods
    -------
    """
    def __init__(self, target=None, random=False, batch_size=1, full=False):

        self._FILES_REPO_PATH = "/Users/elhadjigagnysylla/Desktop/Machine_learning/datasets/taxi/data/taxi_log_2008_by_id"
        self._BATCH_FILE_OUTPUT_PATH = None  # TODO 
        if not target:
            if full:
                raise ValueError("the given value for full parameter is deprecated -- memory restriction")
            if not random:
                raise ValueError("if not target, random must be automatically set to True")
            self.target = target
        else:
            self._target = target 
        self.batch_size = batch_size
        self.full = full 
        self.random = random and self.target is None
        self.tracking_files = [] # set it only for random option 


    def __str__(self):
        
        return "infos -- {}".format(self.__dict__)
        # a simple way to do it ... dict keys must be more explicit 
        # return self.__dict__
    
    def _random_generating(self): # make this function recursive 
        whl = True
        while whl:
            for _ in range(self. batch_size):
                file = os.path.join(self._FILES_REPO_PATH,random.choice(os.listdir(self._FILES_REPO_PATH)))
                self.tracking_files.append(file)
            whl = len(set(self.tracking_files)) != self.batch_size
    
    def fit_batch(self, *args, **kwargs):
        if self.target:
            return 
        # get (batch_size) random files and save their paths into self.tracking_files list 
        self._random_generating()

    def get_csv(self, *args, **kwargs):
        if self.target:
            return self.target 
        else:
            return self.tracking_files

class ProcessingForRS(Processing):
    def __init__(self, target=None, random=False, batch_size=1, full=False, rating="Naive", grid_size=4):
        super().__init__(target=None, random=False, batch_size=1, full=False)
        self.rating = rating
        self.grid_size = grid_size 
    
    def process(self):
        w = {False: self.target, True: self.tracking_files}
        files = w[self.random is True]
        data = []
        for file in files:
            scorer = Naive(file=file, grid_size=self.grid_size)
            scorer.fit()
            data.append(scorer.data)
        return pd.DataFrame(data ,ignore_index=True)

        


     





    
    
    def fit(self):




    

class ProcessingForClustering(Processing):
    def __init__(self, target=None, random=False, batch_size=1, full=False, others=None):
        super().__init__(target=None, random=False, batch_size=1, full=False)
        self.others = others 


