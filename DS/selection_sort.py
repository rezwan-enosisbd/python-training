def selection_sort(li):
  n = len(li)

  for i in range(n-1):
    index_min = i
    for j in range(i+1, n):
      if li[index_min] > li[j]:
        index_min = j
    if index_min != i:
      li[i], li[index_min] = li[index_min], li[i]
  return li

if __name__=='__main__':
  li = [ 10, 3, 11,7, 199]
  print(selection_sort(li))