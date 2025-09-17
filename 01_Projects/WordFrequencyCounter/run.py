import os
import json
import ast
import tabulate
# 2. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# Word Frequency Counter (String + Dict + File I/O)
#
# Read a text file.
#
# Count frequency of each word (case-insensitive).
#
# Save the result to another file as a dictionary.



class WordFrequencyCounter:

    @staticmethod
    def cleanFile(file):
        file.seek(0)
        file.truncate(0)

    @classmethod
    def openFile(cls):
        try:
         fileName = str(input("Enter file name (TXT): WithOut Extension: "))
         if os.path.isfile("./fileDB/"+fileName+".txt"):
            with open("./fileDB/"+fileName+".txt","r+") as file:
                data = file.read()
                UpperCaseData = str(data.upper()).split()
                wordCount = len(UpperCaseData)
                preparedObject = {"fileName": fileName+".txt", "wordCount": wordCount}
                if os.path.isfile("fileDB/AppInternalStorage/record.txt"):
                   with open("fileDB/AppInternalStorage/record.txt", "r+") as systemFile:
                       data = systemFile.read()
                       if data == "":
                           systemFile.write(f"[{preparedObject}]")
                           systemFile.close()
                           return None
                       else:
                           NewTempData = ast.literal_eval(data)
                           newList = list(NewTempData)
                           newList.append(preparedObject)
                           cls.cleanFile(systemFile)
                           systemFile.write(str(newList))
                           print("Data saved")
                           return None
                else:
                    print("System Error")
                    return None
         else:
            print("File not found")
            return  None
        except Exception as e:
            print("System error")
            return None

    @classmethod
    def displayRecord(cls):
        try:
            with open("./fileDB/AppInternalStorage/record.txt", "r+") as systemFile:
                data = systemFile.read()
                if data == "":
                    print("No record frond")
                    return None
                else:
                    NewTempData = ast.literal_eval(data)
                    tableData = tabulate.tabulate(NewTempData, headers="keys", tablefmt="psql")
                    print(tableData)
        except Exception as e:
            print("System error")
            return None

    @classmethod
    def dropRecord(cls):
        try:
            with open("./fileDB/AppInternalStorage/record.txt", "r+") as systemFile:
                systemFile.seek(0)
                systemFile.truncate(0)
                print("Record dropped successfully")
                return None
        except Exception as e:
            print("System error")
            return None


def main():
   print("|_______________________________|")
   print("|Press '1' for new file.        |")
   print("|Press '2' to check record.     |")
   print("|Press '809080' to drop record. |")
   print("|Press '0' to exit program.     |")
   print("|-------------------------------|")

   operationNumber = str(input("Enter Operation number: "))
   if operationNumber == '1':
       WordFrequencyCounter.openFile()
   elif operationNumber == '2':
       WordFrequencyCounter.displayRecord()
   elif operationNumber == '809080':
       WordFrequencyCounter.dropRecord()
   else:
       print("Operation not found")


print("Welcome to world counter!!!")
while True:
    main()