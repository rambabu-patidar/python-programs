# we cannot copy by assigning because then we will have one object and different 
# reference to same obj

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

list3 = list1.copy() # use copy method
print(list3)


list4 = list(list2) # use the list constructor
print(list4)