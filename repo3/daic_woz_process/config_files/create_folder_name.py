from config_files import config as c

EXP_FOLDERS = ['log', 'model', 'condor_logs']

if c.EXPERIMENT_DETAILS['DATASET_IS_BACKGROUND']:
    bkgnd = '_bkgnd'
else:
    bkgnd = ''

if c.EXPERIMENT_DETAILS['FEATURE_EXP'] == 'logmel' or c.EXPERIMENT_DETAILS[
    'FEATURE_EXP'] == 'mel' or c.EXPERIMENT_DETAILS['FEATURE_EXP'] == 'MFCC' or\
        c.EXPERIMENT_DETAILS['FEATURE_EXP'] == 'MFCC_concat':
    if c.EXPERIMENT_DETAILS['DATASET_IS_BACKGROUND']:
        FOLDER_NAME = f"BKGND_{c.EXPERIMENT_DETAILS['FEATURE_EXP']}" \
                      f"_{str(c.EXPERIMENT_DETAILS['FREQ_BINS'])}"
    elif not c.EXPERIMENT_DETAILS['DATASET_IS_BACKGROUND'] and \
            c.EXPERIMENT_DETAILS['REMOVE_BACKGROUND']:
        if c.EXPERIMENT_DETAILS['WHOLE_TRAIN']:
            FOLDER_NAME = f"{c.EXPERIMENT_DETAILS['FEATURE_EXP']}" \
                          f"_{str(c.EXPERIMENT_DETAILS['FREQ_BINS'])}_WHOLE"
        else:
            FOLDER_NAME = f"{c.EXPERIMENT_DETAILS['FEATURE_EXP']}"
    elif not c.EXPERIMENT_DETAILS['DATASET_IS_BACKGROUND'] and not \
            c.EXPERIMENT_DETAILS['REMOVE_BACKGROUND']:
        FOLDER_NAME = f"{c.EXPERIMENT_DETAILS['FEATURE_EXP']}" \
                      f"_{str(c.EXPERIMENT_DETAILS['MEL_BINS'])}_with_backgnd"
elif c.EXPERIMENT_DETAILS['FEATURE_EXP'] == 'raw':
    if c.EXPERIMENT_DETAILS['DATASET_IS_BACKGROUND']:
        FOLDER_NAME = f"BKGND_{c.EXPERIMENT_DETAILS['FEATURE_EXP']}"
    elif not c.EXPERIMENT_DETAILS['DATASET_IS_BACKGROUND'] and \
            c.EXPERIMENT_DETAILS['REMOVE_BACKGROUND']:
        FOLDER_NAME = f"{c.EXPERIMENT_DETAILS['FEATURE_EXP']}"
    elif not c.EXPERIMENT_DETAILS['DATASET_IS_BACKGROUND'] and not \
            c.EXPERIMENT_DETAILS['REMOVE_BACKGROUND']:
        FOLDER_NAME = f"{c.EXPERIMENT_DETAILS['FEATURE_EXP']}_with_backgnd"
else:
    FOLDER_NAME = f"{c.EXPERIMENT_DETAILS['FEATURE_EXP']}"

if c.EXPERIMENT_DETAILS['SNV']:
    if c.EXPERIMENT_DETAILS['DATASET_IS_BACKGROUND']:
        # FOLDER_NAME = FOLDER_NAME + '_bkgnd_svn_exp' # was originally this, but DepAudioNet model expects data to have path _snv_exp
        FOLDER_NAME = FOLDER_NAME + '_bkgnd_snv_exp'
    else:
        # FOLDER_NAME = FOLDER_NAME + '_svn_exp']  # was originally this, but DepAudioNet model expects data to have path _snv_exp      
        FOLDER_NAME = FOLDER_NAME + '_snv_exp'

else:
    if c.EXPERIMENT_DETAILS['DATASET_IS_BACKGROUND']:
        FOLDER_NAME = FOLDER_NAME + '_bkgnd_exp'
    else:
        FOLDER_NAME = FOLDER_NAME + '_exp'
