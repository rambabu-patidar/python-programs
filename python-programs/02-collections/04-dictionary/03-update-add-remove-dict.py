me = {
    "name": "Ram",
    "city": "Ujjain",
    "fav-color": "gold",
    "n": 100,
}

# ____________________UPDATE Or CHANGE______________________

# update by the square brakets
me["fav-color"] = "lightblue"
me["city"] = "Indore"


# update using the update(iterables) method
# The argument must be a dictionary, or an iterable object with key:value pairs.

me.update({"n": 200}) # single item update
me.update({"name": "Balram", "city": "Shajapur"}) # updating multiple item.
print(me)


#____________________________ADD_________________________

# use square bracket to add an item
me["college"] = "JEC"

# update() can also be used to add item if the given argument doesn't exist

me.update({"village": "Chhapri", "dist": "Ujjain"})
print(me)

#______________________REMOVE_______________________

# pop(key) method remove the specified key value pair
me.pop("n")


# popitem() method remove the last entered key: value pair
# note: before 3.7, a random item is removed instead

me.popitem()
print(me) # remove dist: Ujjain key value pair that was last inserted.

# del remove the item with the given key
# del can remove the whole dict
# clear() can empty all the items from dict

del me["college"] # must needed key to remove from my life.
print(me)
me.clear()
print(me)
del me
# print(me) # error