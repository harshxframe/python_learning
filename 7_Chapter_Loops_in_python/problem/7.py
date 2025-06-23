# factorial
from itertools import product

n = int(input("Enter the n number"))
product =1

for i in range(1, n+1):
    product = product*i

print(product)
