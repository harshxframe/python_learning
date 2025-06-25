# write a class "calculator capable ot finding square, cube, and square root of a number"
import math

from wheel.macosx_libfile import calculate_macosx_platform_tag


class Calculator:

      num1 = 0
      # we need three functions
      @staticmethod
      def square(num1):
        return  num1 * num1

      @staticmethod
      def cube(num1):
        return  num1 * num1 * num1

      @staticmethod
      def squareRoot(num1):
        return math.sqrt(num1)

      @staticmethod
      def greet():
          print("Hello Boss! How are you?")





calculator = Calculator()

calculator.greet()

print("Press 1 For square.")
print("Press 2 For Cube.")
print("Press 3 for Square root.")

operation = int(input("Enter a operation number:"))

if operation ==1:
    aInput = int(input("Enter the number for Square: "))
    result = calculator.square(aInput)
    print(result)
if operation ==2:
    aInput = int(input("Enter the number for Cube: "))
    result = calculator.cube(aInput)
    print(result)
if operation ==3:
    aInput = int(input("Enter the number for Square Root: "))
    result = calculator.squareRoot(aInput)
    print(result)






