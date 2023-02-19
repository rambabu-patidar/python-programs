# Lets now do a simple question based on the array

# Q. Find the maximum and minimum item in the given array

nums = [23, 12, 5, 65, 77, 23, 122, 98, 89]

# in-built method way
print(max(nums))
print(min(nums))

# our own way.

def findMin(nums):
    min = 1000000 # keep it as big as you can
    for number in nums:
        if number < min:
            min = number
    return min

def findMax(nums):
    max = -1000000 # keep it as big as you can
    for number in nums:
        if number > max:
            max = number
    return max

print(findMin(nums), findMax(nums))

# Modified

def findMinMax(nums):
    min = 100000
    max = -100000
    for number in nums:
        if number < min:
            min = number
        if number > max:
            max = number
    return [min, max]

print(findMinMax(nums))