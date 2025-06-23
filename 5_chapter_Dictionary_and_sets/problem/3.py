

set1 = set()



set1.add(1)
set1.add("1")


print(set1)


# question next


set1.add(20)
set1.add(20.0)
set1.add(("20.0"))

print(set1)


print(len(set1))