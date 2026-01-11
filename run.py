import datetime
import os
from recursive_unzip import recursive_unzip
from flatten_folder import move_contents_to_root

# Genereate a unique result file name based on the current UTC date and time should look like '2024-06-15_14-30-00'
print("Generating unique result folder name based on current UTC date and time...")
file_name= (datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d_%H-%M-%S'))
print(file_name)

# Create a directory for the extracted contents
print("Creating extraction directory...")
extract_dir = os.path.join('.', 'results', f'{file_name}')
# throws error if directory exists
os.makedirs(extract_dir)

print("Starting recursive unzip of all .zip files in the current directory...")
for entry in os.listdir('./importeddata'):
    if entry.endswith('.zip'):              
        print("Unzipping file:", entry)          
        full_path = os.path.join('./importeddata', entry)
        recursive_unzip(full_path, extract_dir)

## should have all results here
print("Flattening the folder structure...")
move_contents_to_root(extract_dir)

print("Flattening completed.")