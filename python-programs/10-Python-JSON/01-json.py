# JSON is used to store and exhange the data over web
# Working with JSON is easier than object and data types so it is used 
# learn more about it on MDN
# JSON stands for JavaScript Object Notation

# Python has built in package for json

import json

# JSON string
strJSON = '{ "name":"John", "age":30, "city":"New York"}'

# 1. From JSON to python
myDict = json.loads(strJSON)
print(myDict)

# 2. From Python to JSON
strJSON2 = json.dumps(myDict)
print(strJSON2)


# we can convert many data type in JSON
print(json.dumps({"name": "John", "age": 30})) # dict -> Object (JS equivalent)
print(json.dumps(["apple", "bananas"])) # list -> array
print(json.dumps(("apple", "bananas"))) # tuple -> array
print(json.dumps("hello")) # string -> string
print(json.dumps(42)) # integer -> number
print(json.dumps(31.76)) # float -> number
print(json.dumps(True)) # boolean -> true
print(json.dumps(False)) # boolean -> false
print(json.dumps(None)) # none -> null

# print(json.dumps({"apple", "bananas"}))
# json.dumps doesn't support data type "set


myObj = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(myObj))
# but it is not formated

# now it is formatted
print("INDENTED JSON STRING:")
print(json.dumps(myObj, indent=4))

# we can get the sorted JSON string by using sort_keys=True property
print("SORTED JSON STRING:")
print(json.dumps(myObj, indent=4, sort_keys=True))