# Write a python program to print the contents of a directory using the os module.

# Import os module
import os

# specify the directory you want to list
directory = "D:\\Python Course\\Chapter 1"

# list all files and folders in the directory
contents = os.listdir(directory)

# Printing the Content of the directory
print(f"Contents of directory '{os.path.abspath(directory)}':")
for item in contents:
    print(item)
