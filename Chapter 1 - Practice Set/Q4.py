# Q4. Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 

import os
# Specify the directory you want to list
directory_path = '/' # Give directory, only '/' gives all list in C drive.

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# print each file and directory name 
for item in contents:
    print(item)