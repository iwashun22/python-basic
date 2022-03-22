# string can be single quote or double quotes
copyright = "\n\n© Micheal"

print("Hello\n\"World\"")
print(copyright)

# multiple line string
# forward slash is to not make a new line
print("""Line 1
Line \
2""") # Line 1
      # Line 2

phrase = "This iS AwESoMe"
print(phrase.lower()) # this is awesome

print(phrase.isupper()) # False

print(phrase.upper().isupper()) # True

print(len(phrase)) # 15

print(phrase[8]) # A

# specify the beginning and ending
# ** this will not include index 3
print(phrase[1:3]) # hi

# first index can be omit
print(phrase[:4]) # This

# this will print the 2nd index from backward
print(phrase[-2]) # M

# can not reassign the string by index
#  phrase[0] = "t" # <- Error

# can reassign by this way
phrase = 't' + phrase[1:]
print(phrase) # this iS AwESoMe


# find the first index that contain in the parameter
print(phrase.index("i")) # 2 
print(phrase.lower().index("awesome")) # 8

print(phrase.replace("e", "x")) # This iS AwESoMx
print(phrase.lower().replace("is", "lol")) # thlol lol awesome


# Format
word = "Python"
print(f"{word} is fun!") # Python is fun!