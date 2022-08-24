from array import array
arr = array('i', [2,34,534, 23])

for i in range(len(arr)):
  print(arr[i])

from collections import defaultdict, Counter, deque
s1 = 'hello world'
dt = defaultdict(int)
for c in s1:
  dt[c] += 1
print(dt)

c = Counter(s1)
print(c)
print(list(c.elements()))
print(c.most_common(3))
print(c.total())

d = deque()
d.extend([1,2])
print(d)
d.append(99) # 1, 2, 99
d.pop() # 1, 2
d.popleft() # 2
d.appendleft(22) # 22, 2
d.append(1010) # 22, 2 , 1010
print(d)