# string can be single quote or double quotes
copyright = "\n\n© Micheal"

print("Hello\n\"World\"")
print(copyright)

phrase = "This iS AwESoMe"
print(phrase.lower()) # this is awesome

print(phrase.isupper()) # False

print(phrase.upper().isupper()) # True

print(len(phrase)) # 15

print(phrase[8]) # A

# find the first index that contain in the parameter
print(phrase.index("i")) # 2 
print(phrase.lower().index("awesome")) # 8

print(phrase.replace("e", "x")) # This iS AwESoMx
print(phrase.lower().replace("is", "lol")) # thlol lol awesome