
def mydecor(func):
  def insider(*args, **kwargs):
    print(args)
    print(kwargs['message'])
    func(*args)
  return insider

@mydecor
def sayMyName(name):
  print('I am '+ name)

sayMyName('Rezwan', message="Testing Message **kwargs")

import time
def timer(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    func(*args, **kwargs)
    end = time.time()
    print('Function execution time: {:.9f} seconds'.format(end-start))
  return wrapper

@timer
def run(n):
  for i in range(n):
    pass

@timer
def sleeper(sec):
  time.sleep(sec)

run(100)
run(10000)
run(10000000)

sleeper(1)
sleeper(1.2)