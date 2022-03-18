# try to input with float or text

#####################
# number = int(input("Enter an integer number: "))
# print(number)
#####################

# if user puts something that is not the integer, the whole app will crash

# this will catch the error and will be able to handle
# but notice it will include any error type
try:
   number = int(input("Enter an integer number: ")) # Even if this process doesn't have any error it will display the error as "Invalid input"
   print(number)
   zero_division = 10 / 0
except:
   print("Invalid input")

# can specify the error to catch so other errors won't get included
# can have multiple exception
try:
   print("string" + 10)
   zero_division = 10 / 0
except ZeroDivisionError:
   print("Can not divide any number with 0")
except TypeError as err:
   print(err)

# always want to catch the specific error