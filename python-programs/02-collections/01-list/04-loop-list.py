myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# without index looping
for nums in myList:
    print(nums, end=" ")
print() # line break

# indexed looping
for i in range(len(myList)):
    print(myList[i], end=" ")
print()

# while loop looping
i = 0
while i < len(myList):
    print(myList[i], end=" ")
    i += 1
print()

#_________________LIST COMPREHENSION______________________
# Syntax
# newlist = [expression for item in iterable if condition == True]

[print(nums, end=", ") for nums in myList]
print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x] # is "a" is present in the fruit name
print(newlist)

newlist2 = [x for x in fruits if x != "apple"] # return all fruits other than apple
print(newlist2)

# if consition is optional so can be omitted
newlist3 = [x for x in fruits]
print(newlist3)

# NOTE: newlist, newlist2, newlist3 variable are not camel case and they can be difficult to read 
# so it is always good practise to keep your variable readable for you and other also


# iterable in the syntax can be anything that can be iterated 
evenNums = [num for num in range(10) if num % 2 == 0]
print(evenNums)


# The expression is the current item in the iteration,
#  but it is also the outcome, which you 
# can manipulate before it ends up like a list item in the new list:
upperCaseFruits = [fruit.upper() for fruit in fruits]
print(upperCaseFruits)

# expression can contain an condition to modify the output
# return orange if found mango otherwise return the whatever it is
withoutMango = [fruit if fruit != "mango" else "orange" for fruit in fruits]
print(withoutMango)