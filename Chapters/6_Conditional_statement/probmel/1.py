a = int(input("Enter ni. 1: "))
b = int(input("Enter no. 2: "))
c = int(input("NEter no. 3: "))
d = int(input("Enter no. 4: "))



if(a>b and a>c and a>d):
    print("A is bigger than all.")
elif(b>a and b>c and b>d):
    print("B is bigger then all.")
elif(c>a and c>b and c>d):
    print("C is bigger than all.")
elif(d>a and d>b and d>c):
    print("D is bigger than all.")
else:
    print("Issue not resolved.")


