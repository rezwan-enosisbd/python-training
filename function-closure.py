def addition(n1):
  def sum(n2):
    return n1+n2
  return sum


if __name__ == '__main__':
  ten_adder = addition(10)
  thirty_adder = addition(30)

  print(ten_adder(6))
  print(thirty_adder(6))

  print(ten_adder.__closure__) # closure
  print(addition.__closure__) # None , means it's not a closure