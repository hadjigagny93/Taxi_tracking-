"""
some infos of module
"""


import os 
import random 
import csv 


def format(_iterable_):
    # transform iterable variable to list of file path 
    return

class Processing:
    """
    attributes:
    -----------
    

    methods:
    --------
    """


    def __init__(self, target=None, random_=False, batch_size=1, full=False):


        self.__FILES_REPO_PATH = None # TODO 
        self.__BATCH_FILE_OUTPUT_PATH = None  # TODO 

        if not target:
            if full:
                raise ValueError("the given value for full parameter is deprecated -- memory restriction")
            if not random_:
                raise ValueError("if not target, random must be automatically set to True")

            self.__target = target
        else:
            self.__target = format(target)


        self.__batch_size = batch_size 
        self.__full = full 
        self.__random = random_ and self.target is None

        self.tracking_files = [] # set it only for random option 


    def get_attr(self):

        _infos_ = dict([
            ("files repo path", self.__FILES_REPO_PATH),
            ("batch file output path", self.__BATCH_FILE_OUTPUT_PATH),
            ("full parameter", self.__full),
            ("batch size", self.batch_size),
            ("random option", self.__random),
            ])
        return _infos_


    def random_generating(self):

        file = os.path.join(self.__FILES_REPO_PATH,random.choice(os.listdir(self.__FILES_REPO_PATH)))
        if file not in self.tracking_files:
            self.tracking_files.append(file)

        if len(self.tracking_files) == self.batch_size:
            return 
        else:
            self.random_generating


    def fit_batch(self, *args, **kwargs):
        if self.__target:
            return 

        # get (batch_size) random files and save their paths into self.tracking_files list 
        self.random_generating()



    def from_txt_to_csv(self, *args, **kwargs):

        return 



class ProcessingForClustering(Processing):
    pass 

class ProcessingForRS(Processing):
    pass 

