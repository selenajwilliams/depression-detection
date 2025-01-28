import os
import numpy as np

# FEATURE_EXP: logmel, mel, raw, MFCC, MFCC_concat, or text
# WHOLE_TRAIN: This setting is for mitigating the variable length of the data
# by zero padding
# SNV will normalise every file to mean=0 and standard deviation=1
EXPERIMENT_DETAILS = {'FEATURE_EXP': 'mel',
                      'FREQ_BINS': 40,
                      'DATASET_IS_BACKGROUND': False,
                      'WHOLE_TRAIN': False,
                      'WINDOW_SIZE': 1024,
                      'OVERLAP': 50,
                      'SNV': True,
                      'SAMPLE_RATE': 16000,
                      'REMOVE_BACKGROUND': True}
# Set True to split data into genders
GENDER = False
WINDOW_FUNC = np.hanning(EXPERIMENT_DETAILS['WINDOW_SIZE'])
FMIN = 0
FMAX = EXPERIMENT_DETAILS['SAMPLE_RATE'] / 2
HOP_SIZE = EXPERIMENT_DETAILS['WINDOW_SIZE'] -\
           round(EXPERIMENT_DETAILS['WINDOW_SIZE'] * (EXPERIMENT_DETAILS['OVERLAP'] / 100))

if EXPERIMENT_DETAILS['FEATURE_EXP'] == 'text':
    FEATURE_FOLDERS = None
else:
    FEATURE_FOLDERS = ['audio_data', EXPERIMENT_DETAILS['FEATURE_EXP']]

# DATASET = '/path/to/DAIC-WOZ'
# WORKSPACE_FILES_DIR = '/path/to/this/code/directory'
DATASET = '/oscar/data/rbalestr/selena/data/raw_data'
'''*** NOTE: I altered the workspace main dir while the oscar group quota is exceeded 
    in /oscar/data/rbalestr
'''
# WORKSPACE_MAIN_DIR = '/oscar/data/rbalestr/selena/data/processed_data_repo3'
WORKSPACE_MAIN_DIR = '/users/swilli43/scratch/processed_data_repo3'
WORKSPACE_FILES_DIR = '/users/swilli43/thesis/repo3/daic_woz_process'
TRAIN_SPLIT_PATH = os.path.join(DATASET, 'train_split_Depression_AVEC2017.csv')
DEV_SPLIT_PATH = os.path.join(DATASET, 'dev_split_Depression_AVEC2017.csv')
TEST_SPLIT_PATH_1 = os.path.join(DATASET, 'test_split_Depression_AVEC2017.csv')
TEST_SPLIT_PATH_2 = os.path.join(DATASET, 'full_test_split.csv')
# CHANGE THIS TO USE A SPECIFIC TEST FILE
# TEST_SPLIT_PATH = TEST_SPLIT_PATH_1
TEST_SPLIT_PATH = TEST_SPLIT_PATH_2
FULL_TRAIN_SPLIT_PATH = os.path.join(DATASET, 'full_train_split_Depression_AVEC2017.csv')
COMP_DATASET_PATH = os.path.join(DATASET, 'complete_Depression_AVEC2017.csv')
