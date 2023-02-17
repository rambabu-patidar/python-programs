# A set is a collection which is unordered, unchangeable*, and unindexed.
# *Note: Set items are unchangeable, but you can remove items and add new items
# The values True and 1 are considered the same value in sets, 
# and are treated as duplicates

mySet = {1, 2, 3, "Rambabu", "Patidar", 12.8722, True} # Note we have True and 1 simultaneously
print(len(mySet)) # because 1 and True are same length is 1 less than it should be

print(type(mySet))

# set Constructor for creating set from other collections 
mySet2 = set((100, 200, 300, 400, 500)) # double braces are important
print(mySet2)