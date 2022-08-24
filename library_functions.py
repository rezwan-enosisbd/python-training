# sum, max , min
li = [ 3, 4, 5, 11, 44]
print(sum(li))
print(max(li))
print(min(li))

#power , absolute
print(pow(2, 4))
print(abs(-4))

# div mode both
print(divmod(7, 2))

# base number change
num = 17
print(bin(num))
print(oct(num))
print(hex(num))

# reversed
print([x for x in reversed(li)])
print(list(reversed(li)))

#round
import math
print(round(math.pi, 2))
print(round(math.pi, 4))
print(round(math.pi, 5))

# all, any
print(all([5 > 1, 2 == 2, 6 < 20]))
print(any([5 > 1, 22 == 2, 64 < 20]))

# enumerate
for index, item in enumerate(li, start = 1):
  print(index, item)

ids = [ 12, 423, 54234, 123, 3232]
names = [ 'Rezwan', 'Robin', 'Nabin', 'Razon', 'Param']

for item in zip(ids, names):
  print(item)

increase_10_list = map(lambda x: x+10, ids)
print(list(increase_10_list))

even_list = filter(lambda x: x%2 == 0, ids)
print(list(even_list))