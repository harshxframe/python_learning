# write a code to read file and check its contain Twincke world or not.

f = open("poem.txt", "r")

data = f.read()


if data.__contains__("superpose"):
    print("It contain the twinkle")
else:
    print("It does not contain the twinkle")


f.close()

