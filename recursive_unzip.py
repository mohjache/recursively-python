import os
import zipfile


def recursive_unzip(zip_path, extract_to):
    """Recursively unzip files in the given directory."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
      # dumped all contents into result folder
      zip_ref.extractall(extract_to)
      for file_name in zip_ref.namelist():    
         # look through result folder for more zip files    
         file_path = os.path.join(extract_to, file_name)
         if zipfile.is_zipfile(file_path):
             # recursively unzip found zip files
             recursive_unzip(file_path, os.path.splitext(file_path)[0])