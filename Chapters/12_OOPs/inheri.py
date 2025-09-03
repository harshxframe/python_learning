class Engine:
    cc = 45
    power = "3400RPM"
    def getEngine(self):
        print(self.power)

class Electrical:
    ports = 345
    powerSupply = "40V"
    runStatus = True


    def getElectrical(self):
        f = str(self.ports) + self.powerSupply
        print("Electrical function called",f)


class Car(Engine, Electrical):
    CarPower = Engine.power
    CarFeatures = Electrical.ports
    def nullStatement(self):
        super().getElectrical()   # super when come under use when we want to run the parent class method or constructor.
        print("Main Car function executed")
    c = 3




carObj = Car()
carObj.nullStatement()


print(carObj.cc)
print(carObj.powerSupply)