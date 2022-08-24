def addition(n1, n2):
  result = 0

  def add():
      nonlocal result
      result = n1+n2
      print(f'Insider Fucntion : Result : {result}')
  add()
  print('Result: ',result)

if __name__ == '__main__':
  n1, n2 = 10, 5
  addition(n1,n2)