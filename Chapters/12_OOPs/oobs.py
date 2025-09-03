from configparser import ConverterMapping
from errno import EOWNERDEAD


class HarshCompany:
    owner = "Harsh Verma"
    wife = "Mr/Mrs. Ayushi Harsh Verma"
    NetWorth = "500 Billion US Dollar"
    CompanyHeadQuarter = "Harsh Company Headquarter, French"
    CompanyHead = "Harsh Company Head"
    CompanyCoHead = "Ayushi Company Co-Head, French"
    CompanyBank = "Harsh citi Bank"
    CompanyName = "Harsh sparkMind & Technology group of Company"
    CompanyFullManPower = "18 Lakhs"
    WorldRanking = "Top No.1"
    GlobalReach = "179+ countries"

    def postInCompany(self):  # instance of a class pass automatically
        print("Hello", self.owner)

    @staticmethod  # Here because we marked it as It will not use self, No object properties
    def withOutSelf():
        print("Hello Harsh")



# Printing the company details


if __name__ == "__main__":
 CompanyObject = HarshCompany()

 # Who own this company Owner
 print(CompanyObject.owner)
 # Company Name
 print(CompanyObject.CompanyName)
 # Company Networth
 print(CompanyObject.NetWorth)

 # run inner function
 CompanyObject.postInCompany()

 CompanyObject.withOutSelf()
