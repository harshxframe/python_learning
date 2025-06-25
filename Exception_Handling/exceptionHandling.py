class Employee:
        name = "Harsh"
        salary = "34"



print("Starting a process")

try:
  obj = Employee()
  print(int(obj.name))
except ValueError as e:
  print("An error has occurred")
finally:
  print("Closing the process")

