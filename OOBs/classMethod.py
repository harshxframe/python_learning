# It is a way to use class inside a method

class Employee:
    a = 34
    @classmethod  # it will refer  the value from the class directly.
    def show(cls):  # CLS we can say a property which hold the class attribute or refer
        print("Hello Harish Bai!",cls.a)



e = Employee()
e.a = 45

e.show()


print(e.a)