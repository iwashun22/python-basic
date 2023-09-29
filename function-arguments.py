#!/usr/bin/python3

def square(x):
  """Return square of a given number

  Parameters
  ------------
  x : int

  Return -> int
  """ # this is called docstring
  square = x ** 2
  return square

print(square(3)) # 9
# print out document
print(square.__doc__)

# set default value
def custom_print(txt="Hello World", suffix="!"):
  """Print text with a suffix.

  Parameters
  ------------
  txt : str
        text or a message.
  suffix : str
        suffix such as ".,!?"
  
  Return -> void
  """
  print(txt + suffix)
  return

custom_print("hi") # expect: hi!
custom_print("what", "?") # expect: what?
custom_print(suffix=",") # expect: Hello World,

# FIXME: when you provide the arguments without in order, you need to specify or else get an error.
"  ↓↓↓↓↓↓↓↓↓↓↓  "
# custom_print(suffix="!!", "Some Text") # error

custom_print(suffix="!!", txt="Success") # expect: Success!!