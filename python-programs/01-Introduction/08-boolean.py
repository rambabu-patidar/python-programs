# True or False
print(True)
print(False)


# The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(100))


"""
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""

"""
And this all evaluates false.

such as (), [], {}, "", the number 0, and the value None.

And of course the value False evaluates to False.
"""

#One more value, or object in this case, evaluates to False, and
# that is if you have an object that is made from a class with
# a __len__ function that returns 0 or False

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))