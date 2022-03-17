age = input("Enter your age: ")
age = int(age)

if age < 10:
   print("Go home and study.")
elif age < 20:
   print("You can not drink alcohol, you are under age.")
else:
   print("What would you like to order.")

def tall_male(is_tall, is_male):
   if is_tall and is_male:
      print("You are a tall man")
   elif is_tall and not is_male:
      print("You are a tall woman")
   elif not is_tall and is_male:
      print("You are a short man")
   else:
      print("You are a short woman")

tall_male(True, False) # You are a tall woman
tall_male(True, True) # You are a tall man