# list method


friends = ["Apple", "Orange", "Akash", 34, False]

print(friends)

friends.append("Harry") # Add at the end.

print(friends)



# Sorting  using sort and reserve
l1 = [3,43,4,5,65,57,8,89,4,3]

l1.sort() # sort lowest to highest
print(l1)
l1.reverse() # reverse the list
print(l1)



# insert method in this use to insert item on defined index
# task to add intem on index 3

l1.insert(2, 34)

print(l1)



#       POP use to delete particular item and returb the value

l1.pop(2) # use to remove item in list on defined index
print(l1) 


# Remove method


l1.remove(43) # Use to remove value from the list
print(l1)