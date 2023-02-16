myList = [1, 2, 3, 4, 5, 6, 100]
print(myList)

# append at last
myList.append(100)
print(myList)

# insert at particular index
myList.insert(3, 300)
print(myList)

# add any iterable(list, tuples, dict, set) in list using extend() method
tempList = [1.1, 1.2, 1.3, 1.4, 1.5]
myList.extend(tempList)
print(myList)


# remove() remove first specified item
myList.remove(100) # both 100 will not be removed
print(myList)

# pop(index) 
myList.pop(0)
print(myList)

# pop() remove the last item
myList.pop()
print(myList)

# del[index] remove the specified index

# del MyList remove whole list 
# clear(MyList) clear whole list but empty list exist

myList.clear()
print(myList)

del myList # removes completely
# print(myList) # error