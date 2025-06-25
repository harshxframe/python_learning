# Program to generate error if file processing.


try:
 with open("testing.py", 'r') as f:
    data = f.readline()
    print("The Given file first line: ", data)
except FileNotFoundError as e:
    print("The required file does not exist")