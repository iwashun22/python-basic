import random

feet_in_mile = 5280

def get_file_extension(filename):
   return filename[filename.find(".") + 1:]

def get_random_int(num):
   return random.randint(1, num)