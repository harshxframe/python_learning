# Write a code to rename a file
import os

fullpath = "/Users/harsh/python_learning/9_Chapter_file_IO/promlem/"
filename = "namedFile.txt"
newName = "renamedFile.txt"




# performing the renaming operation here

os.rename(os.path.join(fullpath, filename), os.path.join(fullpath, newName))


print("File path renamed!")
