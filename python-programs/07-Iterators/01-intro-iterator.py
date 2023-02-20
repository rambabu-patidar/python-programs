# Iterator in Python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
# The iterator object is initialized using the iter() method. It uses the next() method for iteration.

# __iter__(): The iter() method is called for the initialization of an iterator. This returns an iterator object
# __next__(): The next method returns the next value for the iterable. 
# This method raises a StopIteration to signal the end of the iteration.

# When we use a for loop to traverse any iterable object, 
# internally it uses the iter() method to get an iterator object, which further uses the next() method to iterate over.

myList = [1, 2, 3]
myListItr = iter(myList)

print(next(myListItr))
print(next(myListItr))
print(next(myListItr))
# print(next(myListItr)) # This line will give error because we are already at the end of myList


# We can create our own iterator object and iterate on it

class MyIterObj:
    # setting a limit till we can go
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 10 # to start from 10
        return self
    
    def __next__(self):
        # store the current value
        temp = self.x

        if temp > self.limit:
            raise StopIteration
        
        # increment the value and return the old value
        self.x += 1
        return temp
    
# create a object of the class
myIter = MyIterObj(15)

for number in myIter:
    print(number, end=",")
print()




# Iterating over built-in objects List, Tuples, ect.
myTuple = {1, 2, 3, 4, 5}

for number in myTuple:
    print(number, end=",")
print()

# In the following iterations, the iteration state and iterator variable is managed 
# internally (we can’t see it) using an iterator object to traverse over built-in iterables like list, tuple, dict etc.


# ITERABLE VS ITERATOR
# iterable and iterator are different. The main difference between them is, iterable cannot save the state of the iteration, 
# but whereas in iterators the state of the current iteration gets saved.

# Iterating on iterable
numList = [1, 2, 3, 4]
for num in numList:
    # do something
    pass


# iterating on iterator
# we saw that the iterator saves the state we will see it in this example
tup = {1, 2, 3, 4, 5} # iterable object

tupIter = iter(tup) # iterator object
for index, item in enumerate(tupIter):
    print(item, end=",")
    if index == 2:
        print()
        break

# now the state of tupIter is saved so we can access remaining element
print(next(tupIter))
print(next(tupIter))


# we can iterate on the iterable as many times as we want 
# but iterators can be iterated only once then we have to set them again.
# for eg.

newList = [1, 2, 3, 4, 5,6]

# iterate on iterable 
for num in newList:
    # do something
    pass

for num in newList:
    # do something
    pass

# iterate on iterators
newListIter = iter(newList)
for num in newListIter:
    # do something
    print(num, end=" ")
    # pass

# The below for loop will print nothing as we are already at end.
# to prove this try uncommenting the next line
# print(next(newListIter))

for num in newListIter:
    # do something 
    print(num, end=" ")


    # ** The next article was of Scope of variables which we already covered 
    # see it in introduction folder.