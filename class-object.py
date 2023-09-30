from typing import Any


class Student:
   def __init__(self, name, gpa, age, has_scholar):
      # set private variable by __<var_name>
      self.__name: str = name
      self.__gpa: float = gpa
      self.__age: int = age
      self.__has_scholar: bool = has_scholar

   def on_honer_roll(self) -> bool:
      if self.__gpa >= 3.5:
         return True
      else:
         return False

   def change_grade(self, gpa):
      self.__gpa = gpa

   def get_student_data(self) -> dict:
      data_object = {
         "name": self.__name,
         "age": self.__age,
         "gpa": self.__gpa,
         "has_scholar": self.__has_scholar
      }
      return data_object

student1 = Student("Robert", 2.8, 17, True)
student2 = Student("Emma", 3.9, 16, False)

try:
   print(student1.on_honer_roll())
   print(student2.on_honer_roll())
   student1_data = student1.get_student_data()
   student2_data = student2.get_student_data()
   print("1:", student1_data.get("name"), student1_data.get("gpa"))
   print("2:", student2_data.get("name"), student2_data.get("gpa"))

   student1.change_grade(3.2)
   student1.__name = "Change the name" # no effect

   print(student1.get_student_data().get("name"), student1.get_student_data().get("gpa"))

   # FIXME:
   print(student1.__name, student1.__gpa) # error
except AttributeError:
   pass
