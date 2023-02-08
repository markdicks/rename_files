import os

# specify the path to the folder containing the files to be renamed
folder_path = "/path/to/folder"

# get a list of all the files in the folder
file_list = os.listdir(folder_path)

# loop over each file in the folder
for i, filename in enumerate(file_list):
    # create the new filename by adding a numerical prefix to the original filename
    new_filename = f"{i}_{filename}"
    
    # construct the full file path for the original and new filenames
    old_file_path = os.path.join(folder_path, filename)
    new_file_path = os.path.join(folder_path, new_filename)
    
    # rename the file
    os.rename(old_file_path, new_file_path)
