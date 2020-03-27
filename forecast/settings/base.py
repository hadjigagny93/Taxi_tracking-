import os
import logging

# By default the data is stored in this repository's "data/" folder.
# You can change it in your own settings file.

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
DATA_DIR = os.path.join(REPO_DIR, 'data')
OUTPUTS_DIR = os.path.join(REPO_DIR, 'outputs')
LOGS_DIR = os.path.join(REPO_DIR, 'logs')

def main():
    print(__file__)
    print("REPO_DIR -- {}".format(REPO_DIR))
    print("DATA_DIR -- {}".format(DATA_DIR))
    print("OUTPUTS_DIR -- {}".format(OUTPUTS_DIR))
    print("OUTPUTS_DIR -- {}".format(LOGS_DIR))

if __name__ == "__main__":
    main()
