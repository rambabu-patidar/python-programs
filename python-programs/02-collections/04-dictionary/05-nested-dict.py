# we can have nested dictionaries

students = {
    "stu1" :{
        "name": "Milley",
        "age": 23,
        "grade": "A+",
    },
    "stu2": {
        "name": "Moore",
        "age": 30,
        "grade": "F+",
    },
    "stu3": {
        "name": "Einstein",
        "age": 35,
        "grade": "AA+",
    },
}

print(students)

# we can add different dict to a dict in the following way 
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

children = {
    "child1": child1,
    "child2": child2,
    "child3": child3,
}

print(children)

# To access nested dictionaries use chained square bracket as given below
print(children["child2"]["name"])


# learn more methods of dict in references.