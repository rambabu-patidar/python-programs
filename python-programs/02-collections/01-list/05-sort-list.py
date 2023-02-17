# sort() method 
# if given string it sort lexicographically 
# if given number it sort in ascending order

nums = [19, 23, 12, 54, 75,43]
nums.sort()
print(nums)


fruits = ["pear", "cherry", "strawberry", "banana"]
fruits.sort()
print(fruits)


# Error
# mix = [10, 23, 43, "pear", "cherry", "banana"]
# mix.sort()
# print(mix)


# sort in decending order
fruits.sort(reverse=True)
print(fruits)


# Case sensative and keeps Capital letter ahead of small letters
veggies = ["carrot", "Corrinder", "Raddish", "Methi"]
veggies.sort()
print(veggies)


# CUSTOM sorting
def myFunc(n):
    return n - 10

nums2 = [100, 80, 70, 90, 20, 50]
nums2.sort(key= myFunc) # myFunc will return number and sort will sort it by smallest number first
print(nums2)


# pass Inbuild function to key
veggies.sort(key= str.lower)
print(veggies)

# note the last inbuilt function will work for sorting and will not modify the collection



# Reverse

nums.reverse()
print(nums)