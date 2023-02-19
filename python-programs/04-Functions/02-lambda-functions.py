# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax: [lambda arguments : expression]

sum = lambda a, b: a + b
multiply = lambda a, b: a * b

print(sum(4, 5))
print(multiply(4, 5))

def myFun(n):
    return lambda a: a * n

double = myFun(2) # lambda a : a * 2
print(double(3))

# we can reuse
triple = myFun(3)
print(triple(3))
