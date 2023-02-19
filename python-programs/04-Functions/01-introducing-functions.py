# Python is a block of code that runs when we call it otherwise not
# Function are created to reduce the repeatative code and reusable
# We can pass arguments to function and they will be received as parameter where
# the function is declared.
# We can return result computed in the body of function through "return" keyword

# declaring function
def myFunction():
    print("My name is Rambabu Patidar")

# calling myFunction here
myFunction()


# passing arguments in function and receiving them.
def printMyName(name): # name is a parameter.
    print("My name is " + name)

# calling printMyName(argument) function
printMyName("Rambabu Patidar")

#NOTE: From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.



## Arbitarry Arguments, *args
#If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
# This way the function will receive a ** tuple **(that means we it is ordered,
# unchangeble, and allow duplicates) of arguments,
# and can access the items accordingly

def myNumbers(*args):
    for number in args:
        print(number, end=" ")
    print()

myNumbers(1, 2, 3, 4, 5, 6, 7)


# Keyword Arguments
# Thus far we studied the order of the argument is important in passing them
# but we can use key:value syntax for passing argument and then we
# no need to worry about the order or argument.

def fruits(fruit1, fruit2, fruit3, fruit4, fruit5):
    print(fruit1, fruit2, fruit3, fruit4, fruit5)

fruits(fruit1 = "Orange", fruit2 = "Banana", fruit3 = "Pineapple", fruit4 = "Mango", fruit5 = "Kiwi"); # same order as parameter
fruits(fruit3 = "Orange", fruit5 = "Banana", fruit1 = "Pineapple", fruit4 = "Mango", fruit2 = "Kiwi"); # not in same order as parameter.
# both works fine.

# Arbitray Keyword arguments
# This way the function will receive a dictionary of arguments,

def veggies(**veggie):
    for veg in veggie.values():
        print(veg, end=" ")
    print()

veggies(veg1 = "Carrot", veg2="Raddish", veg3="Corrinder", veg4="green-pulse")

# Default parameter

def defaultExample(country, city = "Indore"):
    print(country, city);

defaultExample("India"); # use the default Indore
defaultExample("India", "Mumbai") # override the Indore city
# Always remeber that the default parameter follow the non-default parameters.


# Pass collection to the function and that is ok
def printList(myList):
    print(myList)

myList = [1, 2, 3, 4, 5, 6, 7]
printList(myList)

# pass keyword if you have empty body in function
# Recursion: A function calling itself and ends with a particular condition is called recursion.
