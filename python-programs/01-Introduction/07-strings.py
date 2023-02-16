# 'hello' is the same as "hello".
 # breaks were inserted as it is like <pre> tag in HTML
multiStr = """This is a multi
            line string
            and we can write it 
            in multiple line and it works
            as good as we can think."""
print(multiStr)

# indexing access is allowed so array like behaviour
# but strings are immutable you can't modify string
name = "Kizza"
print(name[0]) # legal
# name[0] = "P"  # illegel

for char in name:
    print(char)


# length of string
print(len(name)) # 5


# check something in string
s = "You are awesome"
if "awesome" in s:
    print("yes present")
else:
    print("Not present")


# check something is not in string
if "good" not in s:
    print("yes good is not present in string s")
else:
    print("good is present in string")


# return range of character in string
# slicing
myName = "Rambabu Patidar"
print(myName[8:15]) # [8th, 15th) "Patidar"
print(myName[:8]) # Rambabu
print(myName[0:]) # Rambabu Patidar
# last char is -1 index 
print(myName[-7:]) # Patidar 
print(myName[-7:-3])

#modify strings
print(myName.upper())
print(myName.lower())
print(myName.strip()) # remove white space from start and end
print(myName.split(" "))

# concat
print("Rambabu " + " " + "Patidar")


# string Format

# we can't combine string and number
num = 100
# ss = "this is hundred" + num # illegal

# use Format
ss = "This is {}"
newSS = ss.format(num)
print(newSS)

myString = "my name is {} and I am {}"
print(myString.format("Rambabu", 21))

# also we can index
myString2 = "my name is {1} and I am {0}"
print(myString2.format(21, "Rambabu"))

# we can use escape sequence for eg
print("My name is \n Rambabu Patidar \t.")

# learn more string methods.