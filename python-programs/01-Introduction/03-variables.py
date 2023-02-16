# Variable are like boxes in which we can put anything we want for out convinence
# python has no command for Variable declaration

a = 10 # Integer
b = 10.102 # Float
strr = "Rambabu Patidar" # string 
# note: we can place string in double and single quote both and its very ok.
isTrue = True # boolean

# a, b, str, isTrue are the variables.
# variables names are case sensative.
# to know the type of variable we can use:

print(type(strr)) # <class 'str'>


# We can cast the data types to one another

number = int("123")
string = str(1234.21)

print(number, string) # checking it

#______________________________________________________
# Variable Naming convention

# valid namings

a = 10
_ = 100
name = "Rambabu"
my_name = "Rambabu" #snake case
myName = 'Rambabu' # camel case
MyName = "Rambabu" # Pascal case
_marks = 98

# Invalid namings

'''
1ram = 10

overall: Names can't start with number and  
        can't use anything other than a-z, A-Z, 0-9 and _(underscore)
'''

#-------------------------------------------------------

# Assigning variables 

a, b, c = 10, 11, "Rambabu"
x = y = z = 100

# unpack collection 

fruits = ["Orange", "Pineapple", "Mango"]
fruitA, fruitB, fruitC = fruits

#____________________________________________________

# Global and local Variables 

# Global Variables : A variable which is defined outside any function in the body of program
# Local variables: Variables which are defined inside funtions or blocks

globalVar = 100; # global variable

def add():
    localVar = 20
    print(localVar) # legal
    print(globalVar) # legal

print(globalVar) # legal
# print(localVar) # illegal

# if we want to modify global variable inside function we should use keyword 'global'

globalVar2 = 30

def func():
    global globalVar2
    globalVar2 = 1000
    print(globalVar2) # 1000

func() # function call

print(globalVar2) # 1000

# if we want to make variable declared inside the function a global varialble we use global

def func2():
    global localTurnedGlobal
    localTurnedGlobal = 99
    print(localTurnedGlobal)


func2() # we have to call first so that once function run and the variable is declared globally from the function otherwise 
# if trying to access this before the function call will throw an error
print(localTurnedGlobal)
