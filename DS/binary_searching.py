def binary_search(li, x):
  left, right = 0, len(li)-1

  while left <= right:
    mid = left + (right-left)//2

    if li[mid] == x:
      return mid
    elif li[mid] < x:
      left = mid + 1
    elif li[mid] > x:
      right = mid - 1
  return -1


if __name__ == '__main__':
  li = [ 1, 3, 5, 7, 88, 200, 333]

  num = 5
  found_index = binary_search(li, num)
  if found_index == -1:
    print(f'{num} didn\'t found in the list ', li)
  else:
    print(f'{num} found in index : {found_index} ,  ', li)