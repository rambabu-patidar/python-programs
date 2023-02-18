a = 10 
b = 20
c = 15

# 0 
# use single if statement
if a > b:
    print(a)

# 0.1 
# if shorthand
# you only have one line to execute then use it.
if a < b: print("a is less than b")


# 1
# use if else chain 
if a > b:
    print(a)
else:
    print(b)


# 1.1
# shorthand if else
# if you have single line in both if and else block use it
# syntax: [execution_line if condition else execution_line]
# This technique is known as Ternary Operators, or Conditional Expressions.
print(a) if a > b else print(b)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#|________________| |_______________________| |_____________|
#       |                      |                     |
#  if condition          else if condition     else condition


# 2
# use if - elif(else if) - else chain
if a > b:
    print(a)
elif b > c:
    print(b)
else:
    print(c)


# 3
# use if - elif(else if) chain
if a > b:
    print(a)
elif(b > c): 
    print(b)

# we can use any number of elif chain in between 
# but the if and else block will be only one in a single chain


# if we have empty block we have to put "pass" keyword in it for eg.

if a > b:
    pass # important otherwise error will be shown
else:
    print(b)
