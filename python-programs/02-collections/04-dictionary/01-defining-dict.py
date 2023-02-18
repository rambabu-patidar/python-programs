# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, 
# changeable and do not allow duplicates.

myDict = {
    "name": "Rambabu Patidar",
    "age" : 21,
    # "city": "jabalpur", # Error not allowed duplicate.
    "city": "Ujjain",
    "course": "Python",
}

print(myDict)

print(len(myDict))
print(type(myDict))

# dictionary constructor

myDict2 = dict(day = 18, month = "Feb", year = 2023)
print(myDict2)


# Note : As of Python version 3.7, dictionaries are ordered. 
# In Python 3.6 and earlier, dictionaries are unordered.