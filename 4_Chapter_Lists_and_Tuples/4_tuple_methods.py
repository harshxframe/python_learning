tup = ("name", "Harsh", 34, 4533, True)
tup2 = (37,) # required if you are using on;y one value 


print(tup)


# Methods in tuples



nop = tup.count("Harsh")  # this method ude to count the quantity of value

print(nop)

i = tup.index(34) #use to check the index of given item

print(i)



# Concentination of string
co = tup + tup2
print(co)


# Use to repeat the value 
repeat = tup * 4

print(repeat)


# len

print(len(repeat))


# CHeck element

checker = "Harsh" in repeat

print(checker)


# asing tuple value to individual variable

d,x,b,t,y = tup 

print(d)
print(x)
print(b)


# slicing in the tuple as same as list


slicedTule = tup[1:4]

print(slicedTule)