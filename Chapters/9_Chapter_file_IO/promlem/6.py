# make a copy of preexist file of text
import os


path = "/Chapters/9_Chapter_file_IO/promlem/"

with open("clonedText.txt", "r+") as file:
    data = file.read()
    with open(path+"copy.txt", "w") as CopyFile:
        CopyFile.write(data)
        



print("Task Done")


