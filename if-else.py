age = input("Enter your age: ")
age = int(age)

if age < 10:
   print("Go home and study.")
if age < 20:
   print("You can not drink alcohol, you are under age.")
else:
   print("What would you like to order.")

def is_tall_male(is_tall, is_male):
   if is_tall and is_male:
      print("You are a tall man")
   if is_tall and not is_male:
      print("You are a tall woman")