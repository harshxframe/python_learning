from OOPs.oobs import HarshCompany


class Emp:

    def __init__(self, name, car):  # dunder method Which is automatically called, And start with __method__ As you create the instance when you create new object
        self.name = name
        self.car = car
        print("Run on first execution")
        print(self.name)



ClassObject = Emp( "harsh", "Mercedes")

print(ClassObject.name)



# roughCode = HarshCompany()
# vari = roughCode.owner
# print(vari)

