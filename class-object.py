class Student:

   def __init__(self, name, gpa, age, is_good_at_math):
      self.name = name
      self.gpa = gpa
      self.age = age
      self.is_good_at_math = is_good_at_math

   def on_honer_roll(self):
      if self.gpa >= 3.5:
         return True
      else:
         return False

student1 = Student("Robert", 3.1, 17, True)
student2 = Student("Emma", 3.6, 16, False)

print(student1.name, student1.gpa)
print(student2.name, student2.gpa)

print(student1.on_honer_roll())
print(student2.on_honer_roll())