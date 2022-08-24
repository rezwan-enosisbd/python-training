import time

def sleeper_func(sec = 1):
  print('Inside Sleeper')
  time.sleep(sec)

def compute_func():
  print('inside compute func')
  for x in range(1000000):
    _ = pow(x, 123)

for fnc in [sleeper_func, compute_func]:
  t1 = time.perf_counter()
  fnc()
  t2 = time.perf_counter()
  time_spent = t2 - t1
  print(f'Time Spend for {fnc.__name__} is : {time_spent}')

# magic of threading, threading is helpful for I/O tasks
import threading
# calculate without threading
t1 = time.perf_counter()
for _ in range(5):
  sleeper_func()
t2 = time.perf_counter()
time_spent = t2 - t1
print(f'Time Spend 5 times sleeper func : {time_spent}')


thread_list = [ threading.Thread(target=sleeper_func) for _ in range(5)]
t1 = time.perf_counter()
for th in thread_list:
  th.start()
for th in thread_list:
  th.join()
t2 = time.perf_counter()
time_spent = t2 - t1
print(f'Time Spend 5 times sleeper func ( Threading ): {time_spent}')

t1 = time.perf_counter()
for _ in range(5):
  compute_func()
t2 = time.perf_counter()
time_spent = t2 - t1
print(f'Time Spend 5 times compute func : {time_spent}')


thread_list = [ threading.Thread(target=compute_func) for _ in range(5)]
t1 = time.perf_counter()
for th in thread_list:
  th.start()
for th in thread_list:
  th.join()
t2 = time.perf_counter()
time_spent = t2 - t1
print(f'Time Spend 5 times compute func ( Threading ): {time_spent}') # threading doesn't much help in CPU intensive task

