num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

def calculate(_num1, _num2, _op):
   result = 0
   if _op == "+":
      result = _num1 + _num2
   elif _op == "-":
      result = _num1 - _num2
   elif _op == "*":
      result = _num1 * _num2
   elif _op == "/":
      result = _num1 / _num2
   else:
      return "Invalid operator... (+,-,*,/)"
   return round(result, 2)

print(calculate(num1, num2, op))