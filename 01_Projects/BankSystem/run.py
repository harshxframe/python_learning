# 3. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#
# Banking System (OOP + Exception Handling + File I/O)
#
# Create BankAccount class with deposit, withdraw, and balance.
#
# Raise exceptions if withdrawal > balance.
#
# Save all transactions to a file.
import json
import os.path
import datetime
import time
from random import random
from time import sleep

from tabulate import tabulate

class Bank:
    @staticmethod
    def handleDB():
        if os.path.exists("systemDB/systemFile.json"):
            with open("systemDB/systemFile.json", "r+") as f:
                #print("top method running")
                if f.read() == "":
                    json.dump([], f)
                    return True

                else:
                    return True

        else:
            os.makedirs("./systemDB", exist_ok=True)
            with open("systemDB/systemFile.json", "w+") as f:
                #print("secondary method running")
                json.dump({}, f)
                f.close()
                return True

    @staticmethod
    def getUniqueAccountNumber():
        try:
         tempNumber = datetime.datetime.now().timestamp()
         finalAccountNumber = str(tempNumber).replace(":", "").replace("-", "").replace(" ", "").replace(".", "").replace(":", "").strip()
         return finalAccountNumber
        except Exception as e:
         print("Failed to generate Account Number"+str(e))
         return False

    def getObject(self, name, balance, fatherName, address):
        try:
         return {
            "AccountNumber": self.getUniqueAccountNumber(),
            "Name": name.upper(),
            "Balance": balance,
            "FatherName": fatherName.upper(),
            "Address": address.upper(),
            "History": [{
                "Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Description":"Account opening initiation".upper(),
                "TransactionType": "Deposit",
                "AvailableBalance": balance,
                "TransactionAmount": balance,
            }]
        }
        except Exception as e:
         print("Failed to get Account Holder Object"+str(e))
         return False

    def createAccount(self):
        try:
         print("Welcome to Bank System")
         accountHolderName = str(input("Account holder full name: "))
         currentBalance = str(input("Opening deposit balance: "))
         holderFatherName = str(input("Father name: "))
         holderAddress = str(input("Address: "))
         confirmation = str(input("Accept Bank Policy y/n: "))

         if accountHolderName != "" and currentBalance != "" and holderFatherName != "" and holderAddress != "" and currentBalance.isnumeric() :
            if confirmation == "y":
                if self.handleDB():
                    #print("All done")
                    holderObj = self.getObject(accountHolderName, currentBalance, holderFatherName, holderAddress)
                    with open("systemDB/systemFile.json", "r+") as f:
                        data = json.load(f)
                        NewList = data
                        NewList.append(holderObj)
                        f.seek(0)
                        f.truncate()
                        json.dump(NewList, f)
                        f.close()
                        print("Account opened successfully")
                        print("Account Number: "+holderObj["AccountNumber"])

                else:
                    print("DataBase Error!")
            else:
                print("Request cancelled!")
         else:
            print("Detail are not satisfied!")
        except Exception as e:
         print("Failed to Create Account"+str(e))
         return False

    @staticmethod
    def getHistoryObj(transactionDescription,tType, totalBalance, transactionAmount):
        try:
         return {
            "Date" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Description" : transactionDescription.upper(),
            "TransactionType" : tType.upper(),
            "AvailableBalance" : totalBalance,
            "TransactionAmount" : transactionAmount,
         }
        except Exception as e:
         print("Failed to get History Object"+str(e))
         return False

    def depositAmount(self):
        try:
         print("Deposit account")
         accountNumber = str(input("Enter account number: "))
         amount = str(input("Enter deposit amount: "))
         transactionDescription = str(input("Enter transaction description: "))
         print("Request Processing...")
         time.sleep(2)
         if accountNumber != "" and accountNumber.isnumeric() and amount != "" and amount.isnumeric() and str(transactionDescription) and str(transactionDescription) != "" and int(amount) >= 0:
            if self.handleDB():
                with open("systemDB/systemFile.json", "r+") as f:
                    data = json.load(f)
                    for i in data:
                        if i["AccountNumber"] == accountNumber:
                            print("Account Holder name: " + i["Name"])
                            i["Balance"] = int(i["Balance"]) + int(amount)
                            historyList = i["History"]
                            historyList.append(self.getHistoryObj(transactionDescription, "Deposit", i["Balance"], amount))
                            f.seek(0)
                            f.truncate()
                            json.dump(data, f)
                            f.close()
                            print("Transaction Successful!")
                            return True
            else:
                print("Database Error!")
                return False
         else:
            print("Detail are not satisfied!")
            return False
        except Exception as e:
         print("Failed to Deposit Amount"+str(e))
         return False

    def withdrawAmount(self):
        try:
         print("Withdraw Amount")
         accountNumber = str(input("Enter account number: "))
         amount = str(input("Enter Withdraw amount: "))
         transactionDescription = str(input("Enter transaction description: "))
         print("Request Processing...")
         time.sleep(2)
         if accountNumber != "" and accountNumber.isnumeric() and amount != "" and amount.isnumeric() and str(
                transactionDescription) and str(transactionDescription) != "" and int(amount) >= 0:
            if self.handleDB():
                with open("systemDB/systemFile.json", "r+") as f:
                    data = json.load(f)
                    for i in data:
                        if i["AccountNumber"] == accountNumber:
                           print("Account Holder name: "+i["Name"])
                           if int(i["Balance"]) > int(amount):
                              i["Balance"] = int(i["Balance"]) - int(amount)
                              historyList = i["History"]
                              historyList.append(
                                   self.getHistoryObj(transactionDescription, "Withdraw", i["Balance"], amount))
                              f.seek(0)
                              f.truncate()
                              json.dump(data, f)
                              f.close()
                              print("Transaction Successful!")
                              return True
                           else:
                              print("Not sufficient balance!")
                              return False
                    print("Account Not Found!")
                    return False

            else:
                print("Database Error!")
                return False
         else:
            print("Detail are not satisfied!")
            return False
        except Exception as e:
         print("Failed to Withdraw Amount"+str(e))
         return False

    def currentBalance(self):
        try:
         print("Current balance")
         accountNumber = str(input("Enter account number: "))
         print("Request Processing...")
         time.sleep(2)
         if accountNumber != "" and accountNumber.isnumeric():
            if self.handleDB():
                with open("systemDB/systemFile.json", "r+") as f:
                    data = json.load(f)
                    for i in data:
                        if i["AccountNumber"] == accountNumber:
                            print("Holder Name: "+str(i["Name"]))
                            print("Balance Checked Successfully!")
                            print("Account Details =>")
                            print("Balance: "+str(i["Balance"]))
                            return True
                    print("Account Not Found!")
                    return False
            else:
                print("Database Error!")
                return False
         else:
            print("Detail are not satisfied!")
            return False
        except Exception as e:
         print("Failed to fetch Current Balance"+str(e))
         return False

    def bankStatement(self):
        try:
         print("Bank State")
         accountNumber = str(input("Enter account number: "))
         print("Request Processing...")
         time.sleep(2)
         if accountNumber != "" and accountNumber.isnumeric():
            if self.handleDB():
                with open("systemDB/systemFile.json", "r+") as f:
                    data = json.load(f)
                    for i in data:
                        if i["AccountNumber"] == accountNumber:
                            print("Account Details =>")
                            print("Holder Name: "+str(i["Name"]))
                            print("Available Balance: "+str(i["Balance"]))
                            historyList = i["History"]
                            tab = tabulate(historyList, headers="keys", tablefmt="grid")
                            print(tab)
                            return True
                    print("Account Not Found!")
                    return False
            else:
                print("Database Error!")
                return False
         else:
            print("Detail are not satisfied!")
            return False
        except Exception as e:
         print("Failed to fetch Bank Statement"+str(e))
         return False

    def allRecord(self):
        try:
         print("All Record")
         if self.handleDB():
            with open("systemDB/systemFile.json", "r+") as f:
                data = json.load(f)
                recordList = []
                for i in data:
                    recordList.append({"AccountNumber": i["AccountNumber"],"Name": i["Name"], "Balance": i["Balance"]})

                if recordList:
                    tab = tabulate(recordList, headers="keys", tablefmt="grid")
                    print(tab)
                    return True
                else:
                    print("No Records Found!")
                    return False
         else:
            print("Database Error!")
            return False
        except Exception as e:
         print("Failed to fetch records"+str(e))
         return False






bankObject = Bank()

print("Welcome to Harsh Bank-System")
def main():
    print("======================================================================================================================================================")
    print("Press 1 for new A/C || 2 for deposit || 3 for withdraw || 4 for Current balance || 5 for Bank Statement || Press 0 for exit || Press 9 for all Account")
    print("======================================================================================================================================================")
    option = str(input("Enter operation number: "))

    if option == "1":
        bankObject.createAccount()
    elif option == "2":
        bankObject.depositAmount()
    elif option == "3":
        bankObject.withdrawAmount()
    elif option == "4":
        bankObject.currentBalance()
    elif option == '5':
        bankObject.bankStatement()
    elif option == '0':
        exit(0)
    elif option == "9":
        bankObject.allRecord()


while True:
    main()





