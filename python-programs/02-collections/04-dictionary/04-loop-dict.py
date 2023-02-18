me = {
    "name": "Ram",
    "city": "Ujjain",
    "fav-color": "gold",
    "n": 100,
}

# print the key name
for item in me:
    print(item, end=" ")
print()

# print keys 
for key in me.keys():
    print(key, end=" ")
print()

# print the values
for item in me:
    print(me[item], end=" ")
print()


# print values again 
for value in me.values():
    print(value, end=" ")
print()


# both key and value simultaneously
for key, value in me.items():
    print(key + ":" + str(value), end=" ")
print()

#_________________COPY_____________________
# use copy() method to copy dict
# use dict() constructor to copy dict

copyDict = me.copy()
copyDict2 = dict(me)

print(copyDict)
print(copyDict2)