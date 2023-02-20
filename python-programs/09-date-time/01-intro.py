# A date in Python is not a data type of its own, 
# but we can import a module named datetime to work with dates as date objects.

import datetime


date = datetime.datetime.now() # current date.
print(date)

print(date.year)
print(date.month)

# we can create date object using datetime() constructor
# year, month, day are necessary parameter and time is optional

dateToday = datetime.datetime(2023, 2, 20)
print(dateToday)

#The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string

print(dateToday.strftime("%U"))

# see all the code format here : https://docs.python.org/3/library/datetime.html?highlight=datetime#strftime-and-strptime-format-codes