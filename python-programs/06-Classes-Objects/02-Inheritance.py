# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(self.fname, self.lname)

person = Person("Rambabu", "Patidar")
person.printName()


class Student(Person):
    def __init__(self, fname, lname, year):
        # Person.__init__(self, fname, lname) # ***
        super().__init__(fname, lname)
        self.year = year

    def welcome(self):
        return F"Hello, My name is {self.fname} {self.lname} and born in {self.year}"

# *** Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
# instead of using Parent.__init__() method we can use super() function

# Student object

stu = Student("Rambabu", "patidar", 2001)
print(stu.welcome())


# if we have a method in child class that is same as in the super class
# the child class method will take dominance.
# and the super class method will be overriden.

# That is the basic of OOPs we'll see it in more detail later.