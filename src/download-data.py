# data download original python file

import os 
import time
import requests
from bs4 import BeautifulSoup
import sys
from concurrent.futures import ThreadPoolExecutor
import zipfile
import shutil
from collections import defaultdict
import pprint

def download_data(in_path):
    start_time = time.time()
    url = 'https://dcapswoz.ict.usc.edu/wwwdaicwoz/'

    download_dir = f'{in_path}/zips'
    print(f'Downloading DAIC-WOZ dataset to {download_dir}...')

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        print(f'created zips folder at {download_dir}')

    response = requests.get(url) # fetch webpage content

    # print the first 100 chars to check for err code
    # print(f'response type: {type(response)} \nresponse: \n{response.content[0:100]}') 

    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')
    print(f'  {len(links)} links found. ')
    links = [link['href'] for link in links if link['href'].endswith('.zip') or link['href'].endswith('.pdf') or link['href'].endswith('.csv')]
    n_zips = sum(1 for link in links if '.zip' in link)
    print(f'  {len(links)} total files found, comprised of {n_zips} .zip files found and {len(links)-n_zips} misc .pdf and .csv files found')
    # print(f'{len(links)} links ending in .zip, .pdf, or .csv found')

    # print(f'ONLY DOWNLOADING THE FIRST 2 LINKS FOR DEBUGGING PURPOSES...')
    # links = links[:2]

    print(f'  Example of found items to download:')
    [print(f'    {links[i]}') for i in range(0, 2)]

    all_downloaded = True

    for item in links:
        file_name = os.path.join(download_dir, item.split('/')[-1])
        filepath = f'{download_dir}/{file_name}'
        if not os.path.exists(filepath): 
            print(f'{filepath} does not exist, downloading it shortly....')
            all_downloaded = False

    if all_downloaded: # TODO: why isn't this printing out? I'm not downloading anything new...
        print(f' All files are already downloaded to {in_path}/zips. No new files to download.')
        return

    for item in links:
        # define file name, path, and download url
        if not item.startswith('http'):
            file_name = item
            download_url = url + item
        else:
            file_name = os.path.join(download_dir, item.split('/')[-1])
            download_url = item 
        filepath = f'{download_dir}/{file_name}'

        # skip download if the file has already been downloaded into the directory
        if os.path.exists(filepath):
            # print(f'   {file_name} has already been downloaded, skipping it')
            continue

        print(f'Downloading {file_name} of {len(links)} to {download_dir}')
        # try to download the file 
        download_file(download_url, filepath, max_download_attempts=3)

    print('All files downloaded.')
    end_time = time.time()
    total_mins = (end_time - start_time) // 60
    total_secs = (end_time - start_time) % 60
    print(f'Downloading {len(links)} files took {total_mins} m, {round(total_secs, 3)} s')


def download_file(download_url, filepath, max_download_attempts = 3, download_attempt = 0):
        """ Helper function to download a zip file using the requests library 
            If a broken pipe error occurs, it will attempt to download the file again
            up to `max_download_attempts` times
        """
        try:
            with requests.get(download_url, stream=True) as r:
                r.raise_for_status()
                with open(filepath, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
        except (requests.exceptions.RequestException, BrokenPipeError) as e:
            print(f"Failed to download {'/'.join(filepath.rsplit('/')[-2:])} initially, re-attempting for the {download_attempt +1} time")
            if os.path.exists(filepath):
                os.remove(filepath)
            while download_attempt < max_download_attempts:
                download_file(download_url, filepath, max_download_attempts, download_attempt) # could this cause an infinite recursion issue?
                download_attempt += 1
            print(f"Max retries reached. Failed to download {filepath}.")
            raise e  # Raise the error


def unzip_files(in_path, out_path):
    """
    Unzips all .zip files located at in_path (e.g. raw_data/zips)
    For each .zip file (e.g. 303_P.zip) this creates a folder with the name of the .zip file (e.g. 303_P/) and saves
    the contents of the zip file in that folder
    If there are files in the folder that are not .zip files, this skips them
    Corrupted files that cannot be unzipped are added to a list of failed_zips which is printed at the end of the function execution
    
    TODO: FUTURE WORK -- right now I assume non corrupted data, but I should make sure that if I encounter a folder that
    already exists, then it has all the expected files (e.g. doing something like validate_data but on a per-folder basis; as of
    now, validate data does a sweep through all participant files (ending in `_P`) in the directory)
    """
    # dir_prefix # before, dir_prefix represnted the in path & then was modified to represent the outpath...
    failed_zips = []
    # failed_moves = []
    # create a folder to move the .zip files into after extracting them
    print(f'Running unzip files to unzip all .zip files in {in_path}')

    # zip_folder = f'{dir_prefix}zips'

    # check if there are any zip files to be unzipped in this directory for error/sanity checking
    files_ending_in_zip = 0
    for file in os.listdir(in_path):
        if '.zip' in file:
            files_ending_in_zip += 1
    if files_ending_in_zip == 0:
        print(f'No zip files found in directory {in_path}. Have you processed all of them already or listed the wrong directory path?')
        sys.exit()

    num_zip_files =  sum(1 for file in os.listdir(in_path) if '.zip' in file)
    print(f'  {num_zip_files} found in directory')

    all_already_unzipped = True
    for curr_zip_file in os.listdir(in_path):
        if 'zip' not in curr_zip_file:
            continue
        if curr_zip_file == "zips": # skip the zips folder when encountered
            continue
        
        # create a folder contianing the filepath if it doesn't exist
        file_name = os.path.splitext(curr_zip_file)[0] # removes file extension (e.g. .zip, .pdf, etc)
        participant_data_folder = f'{out_path}/{file_name}'

        # NOTE: IF the path exists, THEN it must not have errors because if the files were corrupted or patially
        # downloaded, then the zip file would have errored when trying to unzip
        if os.path.exists(participant_data_folder):
            continue
        else:
            all_already_unzipped = False
            print(f'creating folder: {participant_data_folder}')
            os.makedirs(participant_data_folder)
        
        current_zip_path = f'{out_path}/zips/{curr_zip_file}'
        
        # extract all zip files into the new folder
        try:
            with zipfile.ZipFile(current_zip_path, 'r') as zip_ref:
                zip_ref.extractall(participant_data_folder)
        except Exception as e:
            # print(f'error encountered when unzipping file, skipping to next file')
            print(f'ERROR: Occurred when unzipping file {current_zip_path} \n{e}')
            failed_zips.append(curr_zip_file)
            delete_zip_file(current_zip_path)
            continue 
    
    if all_already_unzipped:
        print(f'  All .zip files were aleady unzipped! No work needs to be done')
    elif len(failed_zips) == 0:
        print(f'  Successfully unziped all files')
    else:
        print(f'failed to unzip {len(failed_zips)} files. The failed zips include: {failed_zips}')


def delete_zip_file(path):
    try:
        os.remove(path)  
        print(f'Deleted failed zip file: {path}')
    except Exception as delete_error:
        print(f'Error deleting file: {path}, error: {delete_error}')


def validate_data(in_path):
    """ Given a path, this checks at all participant folders (e.g. any folder ending in _P) in the directory
        contain the expected files. For example, for participant 303 with folder name 303_P, this will ensure
        that the folder 303_P contains: 
        303_AUDIO.wav     303_CLNF_features3D.txt  303_CLNF_gaze.txt  303_CLNF_pose.txt  303_FORMANT.csv
        303_CLNF_AUs.txt  303_CLNF_features.txt    303_CLNF_hog.bin   303_COVAREP.csv    303_TRANSCRIPT.csv
        For any participants missing files, the participant ID and missing files are saved in a map that is 
        printed at the end
        Returns True if data is valid, False if data is invalid
    """
    print(f'Running validate data to ensure all expected files are present in the dataset...')
    missing_data = defaultdict(list) # maps participant ID --> list of missing files
    # List of expected file suffixes
    expected_files = [
        "AUDIO.wav",
        "CLNF_AUs.txt",
        "CLNF_features3D.txt",
        "CLNF_features.txt",
        "CLNF_gaze.txt",
        "CLNF_hog.bin",
        "CLNF_pose.txt",
        "COVAREP.csv",
        "FORMANT.csv",
        "TRANSCRIPT.csv"
    ]

    # Loop through each folder in the base directory that ends with '_P'
    # folders_to_skip = ['documents', 'util', 'zip']
    for folder_name in os.listdir(in_path):
        folder_path = os.path.join(in_path, folder_name)

        if not os.path.isdir(folder_path) or not folder_name.endswith("_P"):
            continue         
        # Check if it is a directory and ends with '_P'
        # Check for each expected file
        for file in expected_files:
            # Construct the expected filename with the participant number
            participant_id = folder_name.split("_")[0]
            expected_file = f"{participant_id}_{file}"
            expected_file_path = os.path.join(folder_path, expected_file)
            
            # Check if the expected file exists
            if not os.path.isfile(expected_file_path):
                print(f'  participant {participant_id} is missing file: {expected_file_path}')
                if file == "CLNF_hog.bin":
                    alt_path = os.path.join(folder_path, f"{participant_id}_CLNF_hog.txt")
                    if os.path.isfile(alt_path):
                        print(f'  participant {participant_id} has a hog.txt file instead of a hog.bin file')
                        break
                else:
                    missing_data[participant_id].append(expected_file)
    
    if not missing_data:
        print(f'  dataset is valid! No data is missing')
        return True
    else:
        print(f'  The following participants are missing the following files:')
        [print(f'   {k}: {v}') for k, v in missing_data.items()]
        return False


print(f'Running download-data.py...')

path = "/oscar/data/rbalestr/selena/data/raw_data"
download_data(in_path=path) # files will be downloaded into raw_data/zips --> download_data creates zip folder & downloads zip files there 
print()
# oscar_path = "../../scratch/raw_data"
# zips_location = "../../scratch/raw_data/zips"
res = unzip_files(in_path=f'{path}/zips', out_path=path)
print()

missing_data = validate_data(path)

# download_data(download_dir) # for any files that failed, 
# unzip_files(test_dir)


## TO check if any folder in the directory is empty, run:
## find /oscar/data/rbalestr/selena/data/raw_data -type d -empty