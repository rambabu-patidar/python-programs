myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = "This is a string"

#____________________FOR LOOP_____________________

# prints list item
for number in myList:
    print(number, end=" ")
print()

# print list item but using range(startIndex, endIndex, jump)
# [startIndex, endIndex)
# startIndex is the index from where we should start 
# endIndex is the index till where we wanna go but not including it.
# jump is the jump we wanna take everytime, default is 1
for i in range(len(myList)):
    print(myList[i], end=" ")
print()


# starting from 2nd index
for i in range(2, len(myList)):
    print(myList[i], end=" ")
print()

# jump of 2 everytime.
for i in range(0, len(myList), 2):
    print(myList[i], end=" ")
print()

# string as array of characters
for char in s:
    print(char, end=" ")
print()


# break and continue.
# break: used to end the loop at specific point 
# continue : used to skip the current iteration
# examples:
for number in myList:
    if number == 5:
        break
    print(number, end=" ")
print()


for number in myList:
    if number == 5:
        continue;
    print(number, end=" ")
print()


# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Note: Note: The else block will NOT be executed if the loop is stopped by a break statement.


# we can have nested for loops
# if for body is empty use "pass" keyword


#________________________WHILE LOOP_______________________