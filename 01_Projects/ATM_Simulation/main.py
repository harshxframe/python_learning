# 6. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#
# ATM Simulation (Conditional Statements + Loops + Exception Handling)
#
# Build a simple ATM menu: deposit, withdraw, check balance.
#
# Handle invalid inputs with exceptions.


class ATMSimulation:

    def getCard(self):
        print("Processing your card..")
        #Test code show like we are validating card
        valid = {"cardNumber":223223215678536, "cardProvider": "Visa","BankProvider":"SBI", "active":True, "international":True}
        op = str(input("1 Withdraw, 2 Deposit, 3 Check Balance"))
        if op == "1":
            self.withdraw()
        elif op == "2":
            self.deposit()
        elif op == "3":
            self.checkBalance()

    @staticmethod
    def getPin():
        pin = str(input("Enter your 4 digit PIN"))
        return pin


    def withdraw(self):
        try:
         print("Withdrawing..")
         requestedAMount = str(input("Enter amount to withdraw:"))
         if requestedAMount.isnumeric():
            userPin = self.getPin()
            # Simulating fake request that we are verifying card password.
            print("Transaction Processing....")
            isRequestAccept = {"password":True, "amountValid":True, "allow":True, "message":"Transaction successful"}
            if isRequestAccept["password"] and isRequestAccept["allow"] and isRequestAccept["amountValid"]:
                print("Transaction successful")
                print("Collect your amount.")
                isMoneyCollected = True #Sensor responding money is collected as True
                if isMoneyCollected:
                    print("Your amount has been collected.")
                    return True
                else:
                    print("Money not collected. Transaction aborted.") # like we revered transaction
                    return True
            else:
                print("Transaction failed. Transaction aborted.")
                return False
         else:
            print("Invalid amount.")
            return False
        except Exception as e:
            print("Transaction failed. Transaction aborted.")
            return False


    def deposit(self):
        try:
            print("Depositing..")
            requestedAMount = str(input("Enter amount to deposit:"))
            if requestedAMount.isnumeric():
                userPin = self.getPin()
                # Simulating fake request that we are verifying card password.
                print("Transaction Processing....")
                isRequestAccept = {"password": True, "amountValid": True, "allow": True,
                                   "message": "Transaction successful"}
                if isRequestAccept["password"] and isRequestAccept["allow"] and isRequestAccept["amountValid"]:
                    print("Transaction successful")
                    print("Deposit successfully")
                    isMoneyCollected = True  # Sensor responding money is collected as True
                    if isMoneyCollected:
                        print("Your amount has been collected.")
                        return True
                    else:
                        print("Money not collected. Transaction aborted.")  # like we revered transaction
                        return True
                else:
                    print("Transaction failed. Transaction aborted.")
                    return False
            else:
                print("Invalid amount.")
                return False
        except Exception as e:
            print("Transaction failed. Transaction aborted.")
            return False

    @staticmethod
    def checkBalance(self):
        print("Checking balance..")
        try:
            print("Depositing..")
            userPin = self.getPin()
            # Simulating fake request that we are verifying card password.
            print("Transaction Processing....")
            isRequestAccept = {"password": True, "amountValid": True, "allow": True,
                                   "message": "Transaction successful"}
            if isRequestAccept["password"] and isRequestAccept["allow"] and isRequestAccept["amountValid"]:
                 print("Transaction successful")
                 print("Deposit successfully")
                 isMoneyCollected = True  # Sensor responding money is collected as True
                 if isMoneyCollected:
                    print("Your amount has been collected.")
                    return True
                 else:
                    print("Money not collected. Transaction aborted.")  # like we revered transaction
                    return True
            else:
                print("Transaction failed. Transaction aborted.")
                return False
        except Exception as e:
            print("Transaction failed. Transaction aborted.")
            return False


print("Welcome to Harsh's ATM")
def main():
    try:
        crd = str(input("Enter your card y/n:"))
        if crd == "y":
           obj = ATMSimulation()
           obj.getCard()
        else:
            print("Invalid input!")
    except Exception as e:
        print("Transaction aborted.",e)


if __name__ == "__main__":
    while True:
        main()


