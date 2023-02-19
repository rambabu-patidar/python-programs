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
for row in range(5):
    print(str(row) + "->", end=" ")
    for col in range(5):
        print(col, end=" ")
    print();
print()

# if for body is empty use "pass" keyword
for number in range(10):
    pass
else:
    print("For loop executed")


#________________________WHILE LOOP_______________________
#Normal while loop
i = 1
while i <= 10:
    print(i, end=" ")
    i+= 1
print()

# break and continue statement works same in while loop

# while loop also has a else statement that execute after the loop finished successfully
# note that if you break out of the loop then else block of while loop will not run.
i = 1
while i <= 10:
    print(i, end=" ")
    i+= 1
else:
    print()
    print("While loop ran successfully")


# using break inside while
i = 1
while i <= 10:
    if i == 5:break # single line to execute so use if this version
    print(i, end=" ")
    i+= 1
else:
    print("While broke out at 5") # This will not execute as we used break in while loop


# NOTE: Like many other programming language we don't have DO WHILE loop in python.