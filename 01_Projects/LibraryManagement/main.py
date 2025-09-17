import json
import os.path
import uuid

# 7. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++DONE
#
# Library Management (OOP + File I/O + Dict)
#
# Book class with attributes (title, author, available).
#
# Store all books in a file.
#
# User can borrow or return a book (update file).
#
# Use exceptions for unavailable books.

class LibraryManagement:

    basePath = "systemDB"

    def isFileExist(self):
        if os.path.exists(self.basePath):
            if os.path.isfile(self.basePath+"/lib.json"):
                with open(f"{self.basePath}/lib.json", "r") as file:
                    if file.read() != "" or file.read() == "[]":
                        return True
                    return False
            else:
                with open(self.basePath + "/lib.json", "w") as f:
                    json.dump([], f)
                    return True
        else:
            os.makedirs(self.basePath, exist_ok=True)
            if os.path.isfile(self.basePath+"/lib.json"):
                    return True
            else:
                with open(self.basePath + "/lib.json", "w") as f:
                    json.dump([], f)
                    return True

    def addBook(self):
        try:
            print("Add Book")
            title = str(input("Enter Title: "))
            author = str(input("Enter Author: "))
            availability = str(input("Availability Y/N: "))
            if title != "" and author != "" and availability == "Y":
                if self.isFileExist():
                    with open(self.basePath + "/lib.json", "r+") as file:
                        data = json.load(file)
                        barCode = str(uuid.uuid4())  # generating barcode number
                        data.append({"barcodeID": str(barCode), "title": title, "author": author, "availability": True})
                        file.seek(0)
                        file.truncate(0)
                        json.dump(data, file)
                        print("Book Added")
                        return True
                else:
                    print("System error in files.")
                    return False
            else:
                print("Details not satisfied.")
                return False
        except Exception as e:
            print(e)
            return False

    def borrowBook(self):
       try:
           print("Borrow Book")
           scanBarCode = str(input("Scan BarCode: "))
           confirm = str(input("confirm Y/N: "))
           if scanBarCode != "" and confirm == "Y":
               if self.isFileExist():
                   with open(self.basePath + "/lib.json", "r+") as file:
                       data = json.load(file)
                       for barCode in data:
                           if barCode["barcodeID"] == scanBarCode:
                               if not barCode["availability"]:
                                   print("Book already borrowed")
                                   return False
                               else:
                                   barCode["availability"] = False
                                   file.seek(0)
                                   file.truncate(0)
                                   json.dump(data, file)
                                   print("Book Borrowed")
                                   return True


                       print("Book Not Found!")
                       return True
               else:
                   print("System error in files.")
                   return False
           else:
               print("Details not satisfied.")
               return False
       except Exception as e:
           print(e)
           return False

    def takeReturnBook(self):
        try:
            print("Take Return Book")
            scanBarCode = str(input("Scan BarCode: "))
            confirm = str(input("confirm Y/N: "))
            if scanBarCode != "" and confirm == "Y":
                if self.isFileExist():
                    with open(self.basePath + "/lib.json", "r+") as file:
                        data = json.load(file)
                        for barCode in data:
                            if barCode["barcodeID"] == scanBarCode:
                               if not barCode["availability"]:
                                   barCode["availability"] = True
                                   file.seek(0)
                                   file.truncate(0)
                                   json.dump(data, file)
                                   print("Book Returned")
                                   return True
                               else:
                                   print("Book already returned")
                                   return True

                        print("Book Not Found!")
                        return True
                else:
                    print("System error in files.")
                    return False
            else:
                print("Details not satisfied.")
                return False
        except Exception as e:
            print(e)
            return False



print("Welcome to Harsh Library Management")
obj = LibraryManagement()
while True:
    operation = str(input("Choose operation 1. Add Book, 2. Borrow a book, 3. Take return book"))
    if operation == "1":
        obj.addBook()
    elif operation == "2":
        obj.borrowBook()
    elif operation == "3":
        obj.takeReturnBook()