# Check entered number is prime or not



numb = int(input("Enter a number for check:"))

if (numb%numb)==0:
    print("Yes this is a prime number")
else:
    print("This is not prime number")
print(numb%numb)