list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

list3 = list1 + list2;
print(list3)


for nums in list3:
    list1.append(nums) # append() and item in last
print(list1)


list1.extend(list2) # add a collection at the end of list 
print(list1)

# There can be more useful method of list so learn by doing.