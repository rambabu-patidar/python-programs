me = {
    "name": "Ram",
    "city": "Ujjain",
    "fav-color": "gold",
    "n": 100,
}

print(me["name"])
print(me["city"])

print(me.get("fav-color"))
print(me.get("n"))


keys = me.keys() # return the list of all the live keys.
print(keys)
# The word live is important because if we add the item later 
# in the list the keys list will 
# automatically gets updated.

me["fastfood"] = "not tried lot so still unknown"
print(keys) # gets updated automatically.



valuess = me.values() # also return the live list of values of dict.
print(valuess)

me["village"] = "Chhapri" # adding new key value pair
me["fastfood"] = "pizza papperoni" # updating the value for fastfood key

print(valuess) # still all changes are visible so it is live in nature.



# The items() method will return each item in a dictionary, as tuples in a list.
# This is also live in nature so we can update and add new item in dictionary and will 
# be visible in list any time.
myDictToList = me.items();
print(myDictToList)




# checking if the key exist in the dict
if "fastfood" in me:
    print("yes fastfood key is present in the dict")
else:
    print("No fastfood key is not available")