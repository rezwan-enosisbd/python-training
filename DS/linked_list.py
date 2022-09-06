class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next

  def __repr__(self):
    return repr(self.data)


class LinkedList:
  def __init__(self):
    self.head = Node()

  def __repr__(self):
    nodes = []
    current_node = self.head.next

    while current_node:
      nodes.append(repr(current_node))
      current_node = current_node.next
    return ','.join(nodes)

  def append(self, data):
    node = Node(data)

    if self.head.next is None:
      self.head.next = node
      return

    curr_node = self.head.next
    while curr_node.next:
      curr_node = curr_node.next
    curr_node.next = node

  def insert(self, data, new_data):
    pass

  def search(self, item):
    pass

  def remove(self, item):
    pass

  def printList(self):
    curr_node = self.head.next
    while curr_node:
      print(curr_node.data)
      curr_node = curr_node.next


ll = LinkedList()
ll.append(10)
ll.append('Rezwan')
ll.append(True)

ll.printList()