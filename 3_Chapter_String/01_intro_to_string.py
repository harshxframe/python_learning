# String can be defined by three ways
# 'Hey' single line
# "Hey" sigle line
# '''Hey''' multiuple line



# String slicing
# To getting a part of string
# It is a imutable if the defined than canot be changed




name = "Harsh"

fullName = "Harsh" # 0,1,2,3,4,5...   or -1 from rtl

strLen = len(fullName) # to get the length of string

print(strLen)

# positive slicing


finalName = fullName[1:4] # index start and index end last index will not include
print(finalName)



# Negative slicing

print(fullName[-4 : -1])

print(fullName[:4]) # emply means 0
print(fullName[1:]) # empty length     
print(fullName[1:5:2]) # Skil slicing
