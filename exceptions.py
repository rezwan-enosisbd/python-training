num1 = 3
num2 = 0

try:
  result = num1/num2
except ZeroDivisionError:
  print('Dividing by 0 is not allowed')