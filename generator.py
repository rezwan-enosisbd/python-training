def counter():
  for i in range(1, 11):
    yield i
print(counter().__next__())
for i in counter():
  print(i)