print(300.90723)

# this is same as other programming languages
#  + -> add
#  - -> subtract
#  * -> multiply
#  / -> divide
#  % -> modulus (remainder)

# convert to string
my_number = 22

# error
# print("My favorite number is " + my_number)

print("My favorite number is " + str(my_number))

negative_number = -5
# absolute value
print(abs(negative_number)) # 5

print(pow(4, 3)) # 64 <- 4^3

print(max(4, 7)) # 7
print(min(4, 7)) # 4

decimal = 15.8
print(round(decimal)) # 16

# Format

pi = 3.14159265359

# print until 2nd decimal place
print(f"π = {pi:.2f}")

# set max digits to 10 and replace with blank space when short
print(f"π has a value of {pi:10.2f}")