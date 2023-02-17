# Once a tuple is created, you cannot change its values.
# Tuples are unchangeable, or immutable as it also is called.

#_______________ADD IN TUPLE________________
# chaning value in tuple
# Tuple -> List -> Tuple
myTuple = [1, 2, 3, 6, 5]
myTupleList = list(myTuple)
myTupleList[3] = 4
modifiedTuple = tuple(myTupleList)
print(myTuple)
print(modifiedTuple)


# Adding item to tuple
# 1. Tuple -> list -> Tuple
# (try yourself)

# 2. Add tuple to a tuple. This is allowed
firstTuple = (1, 2, 3, 4, 5)
secondTuple = (6, 7, 8, 9, 10)
thirdTuple = (11,) # comma is important 

combinedTuple = firstTuple  + secondTuple + thirdTuple
print(combinedTuple)

# ______________REMOVE FROM TUPLE_________________
# delete using the workaround as directly it is not possible
# Tuple -> List -> Tuple

# or delete whole tuple from program 
deleteThisTuple = [1, 2, 3, "deletedThisTuple"]
print(deleteThisTuple)
del deleteThisTuple
# print(deleteThisTuple) # error