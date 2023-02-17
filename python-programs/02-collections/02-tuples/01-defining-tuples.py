# A tuple is a collection which is ordered and unchangeable and allow duplicate values.
#Tuple items are indexed, the first item has index [0]
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

myTuple = ("apple", "banana", "cherry")
print(myTuple)
print(len(myTuple))
print(type(myTuple))


# Tuple with one item should have comma at last
oneItemTuple = ("Rambabu",)
print(oneItemTuple)


#Tuple constructor
builtTuple = tuple((1, 2, 3, 4, 5, "Ram", "Shyam", "etc"))
print(builtTuple)


# ACCESSING TUPLE IS SAME AS THE LIST
# we can use index 
# positive and negative index both are allowed
# we can access range of tuple using -->  [:] 