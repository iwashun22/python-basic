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

# this will print the 2nd index from backward
print(phrase[-2]) # M

# find the first index that contain in the parameter
print(phrase.index("i")) # 2 
print(phrase.lower().index("awesome")) # 8

print(phrase.replace("e", "x")) # This iS AwESoMx
print(phrase.lower().replace("is", "lol")) # thlol lol awesome