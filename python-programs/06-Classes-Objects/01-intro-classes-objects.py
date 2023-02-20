# Python is OOPs(object oriented programming) based language
# Everything in Python is object that has properties(variable) and methods(function)
# In general variable inside classes are called properties and
# as you can guess general functions inside class are called methods.
# a class is a blueprint for real world project.


class Human:
    hand = 2 # property

    # method
    def humanHands(self):
        print("Human has", self.hand, "hands")


humanObj = Human() # creating an instance of Human class that is also known as Object.
print(humanObj.hand) # accessing the hand property useing dot(.) notation
humanObj.humanHands() # accessing the method



# This was the simplest form of class and object but we are using the hardcoded
# values of hand and this is not reusable so we need some way to initialize the
# values. That's why we do have __init__ method (it is same as the constructor we have in other programming languages)

class Person:
    def __init__(self, name, age):
        self.name = name # automatically created name property and its value is set to name parameter which we will pass
        self.age = age

    # This method is added later don't worry I will point out when I will discuss this.
    def __str__(self):
        return f"{self.name}({self.age})"
# creating object of Person
me = Person("Rambabu", 21)

print(me.name)
print(me.age)

# Note: The __init__() function is called automatically every time the
# class is being used to create a new object.

print(me.__str__()) # Returns the object. Default is : <__main__.Person object at 0x000002CDA0551D30>
# But we can set how we want to see it.
# adding __str__() method in Person class. See that method now.

print(me) # this is same as we call __str__() method
print(me.__str__()) # because internally print is calling __str__() method


# IMPORTANT
# You might be thinking is that what is "self"
# The self parameter is a reference to the current instance(object) of the class, and is used to access variables that belong to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
class MyClass:
    n = 100 # we write varible outside of __init__() method which we don't want to initialize every time and is same for all object of that class.
    def __init__(replaceSelf, standard):
        replaceSelf.standard = standard

    def defineClass(changeSelf):
        return f"This is {changeSelf.standard}th standard and it has {changeSelf.n} students."

# create object and call methods
fifthClass = MyClass(5)
print(fifthClass.defineClass())


# we can modify the properties of the class usig dot notation
fifthClass.n = 500
print(fifthClass.defineClass())

# we can delete the properties of the class using del keyword
# let's first add a property
fifthClass.school = "Keautilya Education Academy Makshi"
print(fifthClass.school) # print the above school name
del fifthClass.school # deletes the school name

# if we want to delete the whole object use del keyword
secondClass = MyClass(2)
print(secondClass.defineClass())
del secondClass

# if you have empty class use "pass" keyword to avoid error
class Olympics:
    pass


# if you are notice we have "f" in front string in defineClass() method.
# They are known as f-strings.
# f-strings begin a string with f or F before the opening quotation mark or triple quotation mark.
# Inside this string, you can write a Python expression between { and } characters that can refer to variables or literal values.
# This is the alternative to format() method of string which takes a lot of effort.
# https://docs.python.org/3/tutorial/inputoutput.html
# examples

a = 100
# myString = "The number is:" + a  # invalid we can't add number with string untill we convert it to string

# so we use format() method
myString = "The number is: {0}"
myFormattedString = myString.format(a)
print(myFormattedString)

# or we can use f-strings
myFString = f"The number is: {a}"
print(myFString)
myFString2 = F"{100 + 20* 30}" # we can use simple expression.