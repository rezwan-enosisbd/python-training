
class Stack:
  def __init__(self):
    self.items = []

  def push(self, data):
    self.items.append(data)

  def pop(self):
    return self.items.pop()

  def is_empty(self):
    if self.items:
      return False
    return True

st = Stack()
st.push(2)
st.push(5)
st.push(35)
st.push(11)

while not st.is_empty():
  print(st.pop())