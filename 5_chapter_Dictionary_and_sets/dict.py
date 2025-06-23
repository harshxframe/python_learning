# we are going to study about dictionary
from distutils.command.clean import clean

marks = {
    "Harry" : 100,
    "Shubham": 45,
    "Rani": 34,
    1: "Hello"
}



print(type(marks))


print(marks["Harry"])  # return error



# mutable
# Inordered



# Methods of dictionary
print(marks.items())

print(marks.keys()) # keys
print(marks.values())

marks.update({"Harry": 99})  # if data found than update or not it will update

print((marks.items()))

print((marks.get("Harry"))) # prints non


# copy

nd = {"new" : "More"}
print(nd.items())
nd.clear()

print(nd.items())



# pop item

newDic = {
    "Name": "Harsh ji",
    "Address": "Achalganj/Unnao",
    "PhoneNumber":91705996511
}

print(newDic)
newList = newDic.pop("PhoneNumber")

print(newDic)

print(len(marks))








