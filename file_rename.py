import os
import glob

# Specify the folder where your jpg files are located
folder_path = './data/test'

# Use glob to get a list of all jpg files in the folder
jpg_files = glob.glob(os.path.join(folder_path, '*.jpg'))

# Loop through the jpg files and rename them
for i, file_path in enumerate(jpg_files, start=1):
    # Construct the new file name
    new_file_name = f"{i}.jpg"
    new_file_path = os.path.join(folder_path, new_file_name)

    # Rename the file
    os.rename(file_path, new_file_path)

print("Files renamed successfully.")