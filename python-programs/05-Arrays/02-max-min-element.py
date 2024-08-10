# Lets now do a simple question based on the array

# Q. Find the maximum and minimum item in the given array

from math
import math


nums = [23, 12, 5, 65, 77, 23, 122, 98, 89]

# in-built method way
print(max(nums))
print(min(nums))

# our own way.

def findMin(nums):
    min = math.inf # keep it as big as you can
    for number in nums:
        if number < min:
            min = number
    return min

def findMax(nums):
    max = -math.inf # keep it as small as you can
    for number in nums:
        if number > max:
            max = number
    return max

print(findMin(nums), findMax(nums))

# Modified

def findMinMax(nums):
    min = math.inf
    max = -math.inf
    for number in nums:
        if number < min:
            min = number
        if number > max:
            max = number
    return [min, max]

print(findMinMax(nums))