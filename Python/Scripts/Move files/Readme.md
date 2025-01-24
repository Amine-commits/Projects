Steps:

    Check if the source drive (G) is accessible.
    Search for files in the source drive (G) that match the pattern "S0*".
    Copy those files to the destination folder (on C drive).


    Explanation:

    os.walk(): This function iterates over all files in the G:/ drive, including files in subdirectories.
    file.startswith("S0"): It checks if the file name starts with "S0".
    shutil.copy(): This copies the file from the source to the destination folder.

Improvements:

    The script assumes all the files you want to copy have names starting with S0. You can modify the pattern to match other parts of the file name.
    The script also creates the destination folder if it doesn’t exist.

How to Run:

    Make sure you replace G:/ with the actual source folder path if it’s different.
    Change C:/Shows/ to the folder where you want to copy the files on your C drive.



Using fuction Shutil : import shutil
using function os : import os
The OS module in Python provides functions for interacting with the operating system.



import os
import shutil

# Source directory (G drive)
source_directory = "G:/"

# Destination directory (C drive, specific folder for shows)
destination_directory = "C:/Shows/"

# Make sure the destination directory exists
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Check for the files and copy them
for root, dirs, files in os.walk(source_directory):
    for file in files:
        if file.startswith("S0"):  # Check if the file name starts with "S0"
            source_file = os.path.join(root, file)  # Full path of the file
            destination_file = os.path.join(destination_directory, file)  # Destination path

            # Copy the file
            try:
                shutil.copy(source_file, destination_file)
                print(f"File copied: {file}")
            except Exception as e:
                print(f"Failed to copy {file}: {e}")
