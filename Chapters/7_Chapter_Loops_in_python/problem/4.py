# Now going to print the table using while loop

table = int(input("Enter the table number: "))

incr = 1

while incr<11:
    print(table,"*",incr,"=",(table*incr))
    incr+=1
