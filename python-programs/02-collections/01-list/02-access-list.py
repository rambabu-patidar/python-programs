myList = ["oranges", "banana", "goseberry"]

# indexed access and modifying are allowed
# negative index are allowed
print(myList[1]) # oranges
myList[1] = "pineapple"
print(myList[1]) # pineapple
print(myList[-1]) # banana


# range of indexes are allowed like [2:4]
# doesn't include the last one but includes the first one
# negative index starts at -1 in last
print(myList[0:1])
print(myList[:])
print(myList[2:])
print(myList[:2])


# check if item exist
if "pineapple" in myList:
    print("yes you have pineapple in your list")
else:
    print("no You don't have pineapple in your list")
