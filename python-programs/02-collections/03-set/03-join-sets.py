# use union() method to join 2 sets in third one
# use update() method to join a set in to another

mySet1 = set(("jan", "feb", "mar", "apr", "may", "jul", "aug"));
mySet2 = set(("jun", "jul", "aug", "sep", "oct"));


mySet3 = mySet1.union(mySet2); # union()
mySet1.update(mySet2) # adding mySet2 to mySet1

print(mySet3)
print(mySet1)

# NOTES : This will discard the duplicate if found in the mergeing of two sets.

# to keep only duplicate after merging we can use intersection_update() method

set1 = {1, 2, 3, 4}
set2 = {1, 4, 5, 6}

# to get a new set of the item present in both the set use intersection(set) method
intersectionSet = set1.intersection(set2)
print(intersectionSet)

set1.intersection_update(set2)
print(set1) # print {1, 4}



# The opposite is also possible that we want to keep all the element but not the intersectioned element
# we use symmetric_difference_update() method

set3 = {1, 2, 3, 4, 5} # 1, 2 are the duplicate element
set4 = {1, 2, 6, 7, 8}

intersectionSet2 = set3.symmetric_difference(set4) # not modified the given set
print(intersectionSet2)

# to modify the given set and find the remaining element 

set3.symmetric_difference_update(set4)
print(set3)

# 1 and True are considered as duplicate values in set. keep in mind

# There are lot more methods to try then as you learn.