def separate():
   print("=======================")

# Loop by a string
for letter in "Hello World!":
   print(letter)
separate()

# Loop through array
hobbies = ["Basketball", "Chess", "Drawing"]
for hobby in hobbies:
   print(f"{hobby}: {len(hobby)}")
separate()

# Loop with number
for i in range(10):
   print(i)
   # this will print until 9, not incluing 10
separate()

for x in range(3, 8):
   print(x)
   # this will start to print from 3 until 7
separate()

for i in range(len(hobbies)):
   print("index [" + str(i) + "]: " + hobbies[i])
separate()