# _____________________ACCESS______________
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
# by using the in keyword.

mySet = {1, 2,3, 4, 5, 6, 7}

for number in mySet:
    print(number, end=" ")
print()

if 4 in mySet:
    print("4 is present in the mySet")
else:
    print("4 is not present int the mySet")


#______________________ADD ITEM_______________
# we know that we can't modify the item in set but we can add new item in set
mySet.add(100)
print(mySet)

# To add any iterable in to a set use update() method

anotherSet = {101, 102, 103, 104}
anotherList = ["Indore", "New York", "Macau", "Amsterdam"]
mySet.update(anotherSet)
mySet.update(anotherList)
print(mySet)

# _________________REMOVE ITEM ____________
# To remove item in set use remove(itemName) or discard(itemName) methods
# 
# difference between two is that remove will give error it itemName item doesn't exist
# and discard(itemName) will not produce any error

mySet.remove("Amsterdam")
# mySet.remove("Bhopal")  # error 

mySet.discard("New York")
mySet.discard("Bhopal") # not error

print(mySet)


# pop() removes a random item from set
# clear() clear and empty the set but doesnot delete it whole
# del myList delete whole list

#__________________LOOPING_______________________
# use for looping to access set items

for item in mySet:
    print(item, end=" ")