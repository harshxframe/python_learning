# Create a class (2-d vector) and use it to create another class representing a 3-d vector
class TwoDVector():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class ThreeDVector(TwoDVector):

   def __init__(self, x, y, z):
       super().__init__(x, y)
       self.z = z


   def performFurtherSolutions(self):
        print(f"x: {self.x}\ny: {self.y}\nz: {self.z}")


obj = ThreeDVector(23,34,45)
obj.performFurtherSolutions()