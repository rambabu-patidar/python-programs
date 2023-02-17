# When we create a tuple, we normally assign values to it.
# This is called "packing" a tuple

myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# similarly we can unpack items from tuple

(a, b, c, d, e, f, g, h, i) = myTuple
print(a, b, c, d, e, f, g, h, i)

# also
(a, b, *restAll) = myTuple
print(a, b, restAll) # restAll will be a list

# also 
(a, *accomodateInMiddle, c) = myTuple
print(a, accomodateInMiddle, c)