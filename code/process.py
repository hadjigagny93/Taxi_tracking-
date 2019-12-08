import os 
import random
import pandas as pd 
from tools import grid_search_city

class Process:

    """
    attributes:
    -----------
    self.tracking_files: list of all tracking files for a batch 
    self.samples_size: number of files 
    self.repository_path: path wher files are stagging in 

    methods:
    --------
    self.file_track:
    self.random_search:
    self.one_file_processing:
    self.several_file_processing:
    self.throw_file_in_dir:
    """
    
    def __init__(self, base_path="/Users/elhadjigagnysylla/Desktop/Machine_learning/Taxi_tracking/Taxi_tracking-/data/T drive taxi/release"):
        try:
            os.path.exists(base_path)
            self.base_path = base_path
        except: 
            raise IsADirectoryError()
        self.tracking_files = []
        self.samples_size = 0 # number of files to process for the training 
        self.repository_path = "/Users/elhadjigagnysylla/Desktop/Machine_learning/Taxi_tracking/Taxi_tracking-/data/T drive processed/"

    def file_track(self, path):
        if path in self.tracking_files:
            raise ValueError("path already given -- choice another one !") 
        else:
            pass 

    def random_search(self):

        file_path = os.path.join(self.base_path,random.choice(os.listdir(self.base_path)))

        if file_path not in self.tracking_files:
            return file_path 
        else:
            self.random_search()

    def one_file_processing(self, file_name=None):
        """
        arguments: file_name: -- txt file name to process
        ---------  file_name could be None, if this occurs then generate a random file and add its name to tracking_files list

        return: a csv format table
        -------
        """
        # starting by a verification if the file is already in repo or not 
        
        if file_name:
            file_path = os.join(base_path, file_name)
            try:
                self.file_track(file_path)
            except: 
                raise FileNotFoundError("file not found")
        else:
            # get arandom file in the list
            file_path = random_search()
        self.tracking_files.append(file_path)
        return pd.read_csv(
            file_path,
            sep=",",
            names=["taxi_id", "time_stamp", "lon", "lat"],
            header=None)

    def several_files_processing(self, *args, **kwargs):
        """
        arguments: args: an iterable contaning files path to process, if None, then get them randomly 
        ---------

        return: a csv output 
        ------
        """
        files = []
        if args:
            if len(args) != self.samples_size:
                raise ValueError("Not matched dimensions")
            else:
                # get all files in specified by args paths 
                try:
                    for _paths_ in args:
                        proceesed_one = self.one_file_processing(file_path=_path_)
                        files.append(processed_one)
                except:
                    raise FileNotFoundError("the giving path dos not exist")
        else:
            for _ in range(self.samples_size):
                proceesed_one = self.one_file_processing()
                files.append(processed_one)
        # Now tranform file list into a csv file 
        combined_file = pd.concat([f for f in file])
        return combined_file 
        
        def throw_file_in_dir(self, csv_output=None, name_file=None):

            """
            get a tuple of data: csv return and file and push the file in default directory 
        
            arguments:
            ---------
            csv_output: several_files_processing methods return 
            name_file: file corresponding name 


            return:
            -------
            feedback: a string that notices  if the file hass already been created and pushed in the
            default directory or not

            """
            return feedback






        




   









     
        





















    








        






    def file_processing(self, path):




        


    
