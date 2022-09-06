class Queue:
  def __init__(self, max_size):
    self.max_size = max_size
    self.items = [0] * max_size
    self.head, self.tail, self.size = 0, 0, 0

  def is_full(self):
    if self.size == self.max_size:
      return True
    return False

  def enqueue(self, data):
    if self.is_full():
      print('Queue is full')
      return
    self.items[self.tail] = data
    self.tail = (self.tail + 1) % self.max_size
    self.size += 1

  def dequeue(self):
    item = self.items[self.head]
    self.head = (self.head + 1) % self.max_size
    self.size -= 1
    return item

  def is_empty(self):
    if self.size == 0:
      return True
    return False



q = Queue(5)
q.enqueue(3)
q.enqueue(9)
q.enqueue(1)
q.enqueue(77)
q.enqueue(88)
q.enqueue(99)
q.enqueue(99)
q.enqueue(99)

print(q.head, q.tail, q.items, q.size)

while not q.is_empty():
  print(q.dequeue())

q.enqueue(33)
print(q.head, q.tail, q.items, q.size)


