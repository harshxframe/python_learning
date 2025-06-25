# Create aclass "Programmer" for storing information of new programmers working at microsoft.


class Programmer:
    def __init__(self,name,age,language,salary):
        self._name = name
        self._age = age
        self._language = language
        self._salary = salary


    def show(self):
        print("Name:",self._name)
        print("Age:",self._age)
        print("Language:",self._language)
        print("Salary:",self._salary)


programmer = Programmer("Harsh verma", 23, "Python", "20000000")
programmer.show()
programmer1 = Programmer("Ayushi verma", 22, "Python", "15000000")
programmer.show()
programmer1.show()