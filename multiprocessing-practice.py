import time
import multiprocessing

def sleeper_func(sec = 1):
  print('Inside Sleeper')
  time.sleep(sec)

def compute_func():
  print('inside compute func')
  for x in range(1000000):
    _ = pow(x, 123)

if __name__ == '__main__':
  for fnc in [sleeper_func, compute_func]:
    t1 = time.perf_counter()
    fnc()
    t2 = time.perf_counter()
    time_spent = t2 - t1
    print(f'Time Spend for {fnc.__name__} is : {time_spent}')

  # magic of multiprocessing, multiprocessing is helpful for CPU tasks
  trial_times = 20

  # calculate without threading
  t1 = time.perf_counter()
  for _ in range(trial_times):
    sleeper_func()
  t2 = time.perf_counter()
  time_spent = t2 - t1
  print(f'Time Spend {trial_times} times sleeper func : {time_spent}')


  process_list = [ multiprocessing.Process(target=sleeper_func) for _ in range(trial_times)]
  t1 = time.perf_counter()
  for th in process_list:
    th.start()
  for th in process_list:
    th.join()
  t2 = time.perf_counter()
  time_spent = t2 - t1
  print(f'Time Spend {trial_times} times sleeper func ( Multiprocessing ): {time_spent}')

  t1 = time.perf_counter()
  for _ in range(trial_times):
    compute_func()
  t2 = time.perf_counter()
  time_spent = t2 - t1
  print(f'Time Spend {trial_times} times compute func : {time_spent}')


  process_list = [ multiprocessing.Process(target=compute_func) for _ in range(trial_times)]
  t1 = time.perf_counter()
  for th in process_list:
    th.start()
  for th in process_list:
    th.join()
  t2 = time.perf_counter()
  time_spent = t2 - t1
  print(f'Time Spend {trial_times} times compute func ( Multiprocessing ): {time_spent}')

