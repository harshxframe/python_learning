#Create a class 'pets' from a class 'Animals' and further create a class 'Dog' from 'Pet'. Ass a method 'bark' to class 'Dog'

class Animal:
    @staticmethod
    def pri():
        print("Welcome to Harsh Pets!")



class Pets(Animal):

    # running dummy constructor for learning
    def __init__(self):
        print("Welcome to dummy contractor")


    @staticmethod
    def pri():
        print("Welcome to Harsh Animal Zoo!")



class Dog(Pets):
    def __init__(self):
     super().__init__()
     super().pri()
     Animal().pri()
    @staticmethod
    def bark():
        print("Bark")




obj1 = Dog()

