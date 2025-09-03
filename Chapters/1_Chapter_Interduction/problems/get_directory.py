#imorting module to perform operation in OS
import os

# Specify the directory you want to list
directory_path = "/"


content = os.listdir(directory_path)

#print the directory

for item in content:
   print(item)