import os

# Use this string to write a brief detail about the current experiment. This
# string will be saved in a logger for this particular experiment
EXPERIMENT_BRIEF = ''' Running EXPERIMENT 5 CUSTOM EXPERIMENT -- Oversampling + Paper Reproduction Params
The following config file is used:
'FEATURE_EXP': 'mel',
'CLASS_WEIGHTS': False,
'USE_GENDER_WEIGHTS': False,
'SUB_SAMPLE_ND_CLASS': True,  # Make len(dep) == len(
# ndep)
'CROP': True,
'OVERSAMPLE': True,
'SPLIT_BY_GENDER': True,  # Only for use in test mode
'FEATURE_DIMENSIONS': 120,
'FREQ_BINS': 40,
'BATCH_SIZE': 20,
'SNV': True,
'LEARNING_RATE': 1e-3,
'SEED': 1000,
'TOTAL_EPOCHS': 100,
'TOTAL_ITERATIONS': 3280,
'ITERATION_EPOCH': 1,
'SUB_DIR': 'exp_4_oversample_and_use_gender_weights',
'EXP_RUNTHROUGH': 5}

'''
                    

# Set to complete to use all the data
# Set to sub to use training/dev sets only
# Network options: custom or custom_att (to use the attention mechanism)
# Set to complete to use all the data
# Set to sub to use training/dev sets only
# Network options: custom or custom_att (to use the attention mechanism)


''' EXPERIMENT 5 -- CUSTOM EXPERIMENT -- Oversampling + Paper Reproduction Params
    Paper Reproduction Params + Oversampling
'''
print(f'running w/ over sapmling + paper reproduction params\n')
EXPERIMENT_DETAILS = {'FEATURE_EXP': 'mel',
                      'CLASS_WEIGHTS': False,
                      'USE_GENDER_WEIGHTS': False,
                      'SUB_SAMPLE_ND_CLASS': True,  # Make len(dep) == len(
                      # ndep)
                      'CROP': True,
                      'OVERSAMPLE': True,
                      'SPLIT_BY_GENDER': True,  # Only for use in test mode
                      'FEATURE_DIMENSIONS': 120,
                      'FREQ_BINS': 40,
                      'BATCH_SIZE': 20,
                      'SNV': True,
                      'LEARNING_RATE': 1e-3,
                      'SEED': 1000,
                      'TOTAL_EPOCHS': 100,
                      'TOTAL_ITERATIONS': 3280,
                      'ITERATION_EPOCH': 1,
                      'SUB_DIR': 'exp_5_oversample',
                      'EXP_RUNTHROUGH': 5}



''' EXPERIMENT 4 -- CUSTOM EXPERIMENT -- Oversampling + Gender Weights
    Paper Reproduction Params + USING GENDER WEIGHTS + Oversampling
'''
# print(f'running w/ over sapmling + use gender weights + paper reproduction params\n')
# EXPERIMENT_DETAILS = {'FEATURE_EXP': 'mel',
#                       'CLASS_WEIGHTS': False,
#                       'USE_GENDER_WEIGHTS': True,
#                       'SUB_SAMPLE_ND_CLASS': True,  # Make len(dep) == len(
#                       # ndep)
#                       'CROP': True,
#                       'OVERSAMPLE': True,
#                       'SPLIT_BY_GENDER': True,  # Only for use in test mode
#                       'FEATURE_DIMENSIONS': 120,
#                       'FREQ_BINS': 40,
#                       'BATCH_SIZE': 20,
#                       'SNV': True,
#                       'LEARNING_RATE': 1e-3,
#                       'SEED': 1000,
#                       'TOTAL_EPOCHS': 100,
#                       'TOTAL_ITERATIONS': 3280,
#                       'ITERATION_EPOCH': 1,
#                       'SUB_DIR': 'exp_4_oversample_and_use_gender_weights',
#                       'EXP_RUNTHROUGH': 5}



''' EXPERIMENT 3 -- CUSTOM EXPERIMENT -- TESITNG USING GENDER WEIGHTS
    Setting USE_GENDER_WEIGHTS: True
'''
# print(f'running w/ USE_GENDER_WEIGHTS = True +  paper reproduction params')
# EXPERIMENT_DETAILS = {'FEATURE_EXP': 'mel',
#                       'CLASS_WEIGHTS': False,
#                       'USE_GENDER_WEIGHTS': True,
#                       'SUB_SAMPLE_ND_CLASS': True,  # Make len(dep) == len(
#                       # ndep)
#                       'CROP': True,
#                       'OVERSAMPLE': False,
#                       'SPLIT_BY_GENDER': True,  # Only for use in test mode
#                       'FEATURE_DIMENSIONS': 120,
#                       'FREQ_BINS': 40,
#                       'BATCH_SIZE': 20,
#                       'SNV': True,
#                       'LEARNING_RATE': 1e-3,
#                       'SEED': 1000,
#                       'TOTAL_EPOCHS': 100,
#                       'TOTAL_ITERATIONS': 3280,
#                       'ITERATION_EPOCH': 1,
#                       'SUB_DIR': 'exp_3_using_gender_weights',
#                       'EXP_RUNTHROUGH': 5}


''' EXPERIMENT 2 -- PAPER REPRODUCTION PARAMS
    These experiment details are taken from the github's readme, and were 
    used by the creators of this code base to reproduce the accuracy in the
    DepAudioNet paper this code base is reproducing. See more info here:
    https://github.com/adbailey1/DepAudioNet_reproduction?tab=readme-ov-file
'''
# print(f'running w/ original paper experiment details')
# EXPERIMENT_DETAILS = {'FEATURE_EXP': 'mel',
#                       'CLASS_WEIGHTS': False,
#                       'USE_GENDER_WEIGHTS': False,
#                       'SUB_SAMPLE_ND_CLASS': True,  # Make len(dep) == len(
#                       # ndep)
#                       'CROP': True,
#                       'OVERSAMPLE': False,
#                       'SPLIT_BY_GENDER': True,  # Only for use in test mode
#                       'FEATURE_DIMENSIONS': 120,
#                       'FREQ_BINS': 40,
#                       'BATCH_SIZE': 20,
#                       'SNV': True,
#                       'LEARNING_RATE': 1e-3,
#                       'SEED': 1000,
#                       'TOTAL_EPOCHS': 100,
#                       'TOTAL_ITERATIONS': 3280,
#                       'ITERATION_EPOCH': 1,
#                       'SUB_DIR': 'exp_1',
#                       'EXP_RUNTHROUGH': 5}


''' EXPERIMENT 1 -- DEFAULT PARAMS
    These are the built in parameters for config 1 that come when you clone 
    the repo. Their readme lists different experiment details (see above) 
    which they used to reproduce the DepAudioNet results 
    Hopefully those will increase the accuracy and reduce overfitting!
'''
# print(f'running w/ low acc experiment details')
# EXPERIMENT_DETAILS = {'FEATURE_EXP': 'mel',
#                       'CLASS_WEIGHTS': False,
#                       'USE_GENDER_WEIGHTS': False,
#                       'SUB_SAMPLE_ND_CLASS': True,  # Make len(dep) == len(
#                       # ndep)
#                       'CROP': True,
#                       'OVERSAMPLE': False,
#                       'SPLIT_BY_GENDER': False,  # Only for use in test mode
#                       'FEATURE_DIMENSIONS': 120,
#                       'FREQ_BINS': 40,
#                       'BATCH_SIZE': 20,
#                       'SNV': True,
#                       'LEARNING_RATE': 1e-3,
#                       'SEED': 1000,
#                       'TOTAL_EPOCHS': 100,
#                       'TOTAL_ITERATIONS': 3280,
#                       'ITERATION_EPOCH': 1,
#                       'SUB_DIR': 'exp_2_default_params',
#                       'EXP_RUNTHROUGH': 5}


# Determine the level of crop, min file found in training set or maximum file
# per set (ND / D) or (FND, MND, FD, MD)
MIN_CROP = True
# Determine whether the experiment is run in terms of 'epoch' or 'iteration'
ANALYSIS_MODE = 'epoch'

# How to calculate the weights: 'macro' uses the number of individual
# interviews in the training set (e.g. 31 dep / 76 non-dep), 'micro' uses the
# minimum number of segments of both classes (e.g. min_num_seg_dep=35,
# therefore every interview in depressed class will be normalised according
# to 35), 'both' combines the macro and micro via the product, 'instance'
# uses the total number of segments for each class to determine the weights (
# e.g. there could be 558 dep segs and 440 non-dep segs).
WEIGHT_TYPE = 'instance'

# Set to 'm' or 'f' to split into male or female respectively
# Otherwise set to '-' to keep both genders in the database
GENDER = '-'

# These values should be the same as those used to create the database
# If raw audio is used, you might want to set these to the conv kernel and
# stride values
WINDOW_SIZE = 1024
HOP_SIZE = 512
OVERLAP = int((HOP_SIZE / WINDOW_SIZE) * 100)

FEATURE_FOLDERS = ['audio_data', 'logmel']
EXP_FOLDERS = ['log', 'model', 'condor_logs']

if EXPERIMENT_DETAILS['FEATURE_EXP'] == 'text':
    FEATURE_FOLDERS = None
else:
    FEATURE_FOLDERS = ['audio_data', 'logmel']
EXP_FOLDERS = ['log', 'model', 'condor_logs']

if EXPERIMENT_DETAILS['FEATURE_EXP'] == 'logmel' or EXPERIMENT_DETAILS[
    'FEATURE_EXP'] == 'MFCC' or EXPERIMENT_DETAILS['FEATURE_EXP'] == \
        'MFCC_concat':
    if EXPERIMENT_DETAILS['DATASET_IS_BACKGROUND']:
        FOLDER_NAME = f"BKGND_{EXPERIMENT_DETAILS['FEATURE_EXP']}" \
                      f"_{str(EXPERIMENT_DETAILS['FREQ_BINS'])}"
    elif not EXPERIMENT_DETAILS['DATASET_IS_BACKGROUND'] and \
            EXPERIMENT_DETAILS['REMOVE_BACKGROUND']:
        FOLDER_NAME = f"{EXPERIMENT_DETAILS['FEATURE_EXP']}_{str(EXPERIMENT_DETAILS['FREQ_BINS'])}"
    elif not EXPERIMENT_DETAILS['DATASET_IS_BACKGROUND'] and not \
            EXPERIMENT_DETAILS['REMOVE_BACKGROUND']:
        FOLDER_NAME = f"{EXPERIMENT_DETAILS['FEATURE_EXP']}" \
                      f"_" \
                      f"{str(EXPERIMENT_DETAILS['FREQ_BINS'])}_with_backgnd"
else:
    FOLDER_NAME = f"{EXPERIMENT_DETAILS['FEATURE_EXP']}"

if EXPERIMENT_DETAILS['SNV']:
    FOLDER_NAME = FOLDER_NAME + '_snv_exp'
else:
    FOLDER_NAME = FOLDER_NAME + '_exp'

if EXPERIMENT_DETAILS['USE_GENDER_WEIGHTS']:
    EXPERIMENT_DETAILS['SUB_DIR'] = EXPERIMENT_DETAILS['SUB_DIR'] + '_gen'


DATASET = '/oscar/data/rbalestr/selena/data/raw_data/'
WORKSPACE_MAIN_DIR = '/users/swilli43/scratch/processed_data_repo3'
# WORKSPACE_MAIN_DIR = '/oscar/data/rbalestr/selena/data/processed_data_repo3/'
WORKSPACE_FILES_DIR = '/users/swilli43/thesis/repo3/DepAudioNet_reproduction'
TRAIN_SPLIT_PATH = os.path.join(DATASET, 'train_split_Depression_AVEC2017.csv')
DEV_SPLIT_PATH = os.path.join(DATASET, 'dev_split_Depression_AVEC2017.csv')
# TEST_SPLIT_PATH = os.path.join(DATASET, 'test_split_Depression_AVEC2017.csv')
TEST_SPLIT_PATH = os.path.join(DATASET, 'full_test_split.csv')
FULL_TRAIN_SPLIT_PATH = os.path.join(DATASET, 'full_train_split_Depression_AVEC2017.csv')
COMP_DATASET_PATH = os.path.join(DATASET, 'complete_Depression_AVEC2017.csv')

# DATASET = '/path/to/DAIC-WOZ/dataset'
# WORKSPACE_MAIN_DIR = '/path/to/save/experiment/outputs'
# WORKSPACE_FILES_DIR = '/path/to/depaudionet/code'
# TRAIN_SPLIT_PATH = os.path.join(DATASET, 'train_split_Depression_AVEC2017.csv')
# DEV_SPLIT_PATH = os.path.join(DATASET, 'dev_split_Depression_AVEC2017.csv')
# # TEST_SPLIT_PATH = os.path.join(DATASET, 'test_split_Depression_AVEC2017.csv')
# TEST_SPLIT_PATH = os.path.join(DATASET, 'full_test_split.csv')
# FULL_TRAIN_SPLIT_PATH = os.path.join(DATASET, 'full_train_split_Depression_AVEC2017.csv')
# COMP_DATASET_PATH = os.path.join(DATASET, 'complete_Depression_AVEC2017.csv')


# /oscar/data/rbalestr/selena/data/processed_data_repo3/
