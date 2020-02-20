import os 
import random 
import csv 

def transform(iterable):
    # transform iterable variable to list of file path 
     return iterable

class Processing:
    """
    attributes:
    -----------
    methods:
    --------
    """
    def __init__(self, target=None, random_=False, batch_size=1, full=False):

        self._FILES_REPO_PATH = None # TODO 
        self._BATCH_FILE_OUTPUT_PATH = None  # TODO 
        if not target:
            if full:
                raise ValueError("the given value for full parameter is deprecated -- memory restriction")
            if not random_:
                raise ValueError("if not target, random must be automatically set to True")
            self._target = target
        else:
            self._target = transform(target)
        self._batch_size = batch_size 
        self._full = full 
        self._random = random_ and self.target is None
        self.tracking_files = [] # set it only for random option 

    def get_attr(self):
        _infos_ = dict([
            ("files repo path", self._FILES_REPO_PATH),
            ("batch file output path", self._BATCH_FILE_OUTPUT_PATH),
            ("full parameter", self._full),
            ("batch size", self._batch_size),
            ("random option", self._random),
            ])
        return _infos_
        # a simple way to do it ... dict keys must be more explicit 
        # return self.__dict__

    def random_generating(self):
        file = os.path.join(self.__FILES_REPO_PATH,random.choice(os.listdir(self.__FILES_REPO_PATH)))
        if file not in self.tracking_files:
            self.tracking_files.append(file)
        if len(self.tracking_files) == self.batch_size:
            return 
        else:
            self.random_generating

    def fit_batch(self, *args, **kwargs):
        if self._target:
            return 
        # get (batch_size) random files and save their paths into self.tracking_files list 
        self.random_generating()

    def get_csv(self, *args, **kwargs):
        return 


class ProcessingForClustering(Processing):
    pass 


class ProcessingForRS(Processing):
    pass 

