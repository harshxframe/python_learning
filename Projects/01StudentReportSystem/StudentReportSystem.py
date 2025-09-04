import os
import uuid
from datetime import datetime
from dis import dis
import ast
from tabulate import tabulate


# 1.Student Report System (File I/O + Functions + Loops + Dicts)
#
# Build a program to manage student grades.
#
# Read student data (name, subject, marks) from a file.
#
# Store them in a dictionary.
#
# Allow user to: add new student, update marks, calculate average.
#
# Handle file saving + exceptions.


class Utils:
    @staticmethod
    def getUniqueId():
        uniqueId = str(uuid.uuid4())
        return uniqueId


class StudentReportSystem(Utils):
    @staticmethod
    def saveInfile(self, datObject):
        # create file
        try:
            with open("./fileDB/students.txt", "r+") as file:
                data = file.read()
                if data == "":
                    file.write(str(f"[{datObject}]"))
                    print("Data saved")
                else:
                    tempData = ast.literal_eval(data)
                    tempData.append(datObject)
                    file.seek(0)
                    file.truncate(0)
                    file.write(str(tempData))
                    print("Data saved")
        except Exception as e:
            print("Failed to save file.")

    @staticmethod
    def getFile(self):
        try:
            with open("./fileDB/students.txt", "r") as file:
                data = file.read()
                if data == "":
                    return None
                else:
                    return ast.literal_eval(data)
        except Exception as e:
            return None

    def ShowAllStudents(self):
        try:
            getFile = self.getFile(self)
            tab = tabulate(getFile,headers="keys", tablefmt="grid")
            print(tab)
        except Exception as e:
            print("Failed to show all students.")

    @staticmethod
    def updateMarksInfile(Id, marks):
        try:
            with open("./fileDB/students.txt", "r+") as file:
                data = file.read()
                if data == "":
                    return False
                else:
                    tempData = ast.literal_eval(data)
                    for student in tempData:
                        if student["id"] == Id:
                            student.update({"marks":marks})
                            file.seek(0)
                            file.truncate(0)
                            file.write(str(tempData))
                            return True

                return False

        except Exception as e:
            print("Failed to update marks.",e)
            return False

    def addStudent(self):  # Done
        name = str(input("Enter student name: "))
        subject = str(input("Enter subject name: "))
        marks = str(input("Enter marks: "))
        dataObject = {"id": Utils.getUniqueId(), "name": name, "subject": subject, "marks": marks}
        self.saveInfile(self, dataObject)

    def updateStudent(self):
        stuId = str(input("Enter student Id: "))
        marks = str(input("Enter marks: "))
        res = self.updateMarksInfile(stuId, marks)
        if res:
            print("Marks Updated successfully.")
        else:
            print("Failed to update marks.")
    @staticmethod
    def averageMarks():
        try:
          with open(f"./fileDB/students.txt", "r") as file:
            data = file.read()
            if data == "":
                return False
            else:
             # formula
             tempData = ast.literal_eval(data)
             maxLen = len(tempData)
             avg = 0
             for student in tempData:
                 avg = avg + int(student["marks"])
             print("Average marks: ", avg/maxLen)
             return False
        except Exception as e:
            print("Failed to calculate average marks.")

    @staticmethod
    def dropData():
        try:
            confirm = input("Do you want to drop students data? [y/n]: ")
            if confirm == 'y':
               with open(f"./fileDB/students.txt", "r+") as file:
                 file.seek(0)
                 file.truncate(0)
                 print("Data Dropped")
            else:
                print("Request Canceled.")

        except Exception as e:
            print("Failed to drop data.")



we = StudentReportSystem()


def main(operationChoice):
    if operationChoice == "1":  # to add student
        we.addStudent()
    elif operationChoice == "2":  # showAll Students
        we.ShowAllStudents()
    elif operationChoice == "3":
        we.updateStudent()
    elif operationChoice == "4":
        we.averageMarks()
    elif operationChoice == "0":
        exit(0)
    elif operationChoice == "809080":
        we.dropData()
    else:
        print("Invalid operation")


if __name__ == '__main__':
    while True:
        print("|---------------------------------|")
        print("| Press '1' to add student.       |")
        print("| Press '2' to Show all students. |")
        print("| Press '3' to update student.    |")
        print("| Press '4' to Average marks.     |")
        print("| Enter '809080' to Drop student. |")
        print("| Press '0' to exit program.     |")
        print("|---------------------------------|")
        UserChoice = str(input("Enter your choice: "))
        main(UserChoice)

