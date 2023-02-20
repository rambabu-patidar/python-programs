import greet 
import person 

import platform # built-in module in python
# we can import wither another name that is alias to the module
# import greet as greetModule

# we can import a part of the module also without importing whole module
# from utilityFile import greeAll
from utilityFile import greetAll, myDict, myList


greet.greeting("Rambabu Patidar")

# creating object 
myFriend = person.Person("Balram Patidar")

print(myFriend.name)

# accessing variable from person.py module
print(person.myName)

# using built-in method
print(platform.system()) # windows.

# to list all the function and variable in particular module use dir() method
print(dir(person)) # return list of all stuff.

# using some part of utility module
# note that we now don't have to use the class name in front of it
greetAll()
print(myDict)
print(myList)


# a good read to understand more when we have same name of function and varibles.
# https://www.quora.com/Can-python-distinguish-two-different-functions-defined-with-the-same-name-but-imported-from-different-modules