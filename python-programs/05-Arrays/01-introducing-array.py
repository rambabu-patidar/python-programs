# Python does not have built-in Array support so we will use Lists as arrays
# To work with arrays we have to import numpy library

nums = [1, 2, 3, 4, 5, 6]

# Google why do we need array. what the requirement variables cannot fullfill
# so that we need arrays. This is all about theory which I know so you can google
# it if you want (or I say you must know it before procedding)

thirdNum = nums[2] # accessing
thirdNum =  1000 # modifying
length = len(nums) # length

for number in nums:
    # do whatever in body.
    pass

nums.append(7) # add item in array
nums.pop(0) # takes index and remove the item
nums.remove(2) # takes value and remove it ( remove the first occurence only)

# There are lot of methods array/ List support have a look at the references
