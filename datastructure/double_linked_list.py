class Node(object):

  def __init__(self, value):
    self.prev = None
    self.value = value
    self.next = None

class LinkedList(object):

  def __init__(self):
    self.head = None

  def insert(self, node):
    if self.head:
      self.head.next = node
      node.prev = self.head
      self.head = node
    else:
      self.head = node

  def size(self):
    c = 1
    current = self.head
    while current.prev:
      current = current.prev
      c += 1
    return "double linked list size %s" % (c,)

  def delete(self, node):
    if self.size() == 0:
      raise ValueError("Nothing is there to delete.")
    elif self.head == node:
      self.head = self.head.prev
      return "deleted Node %s" % (self.head.value)
    else:
      current = self.head
      while current:
        if current == node:
          print "delete",current.value
          lead_node = current.next
          lag_node = current.prev
          lead_node.prev = lag_node
          lag_node.next = lead_node
          print "deleted Node %s" % (current.value,)
          break
        else:
          current = current.prev

  def print_list(self):
    current = self.head
    while current:
      print "node value:", current.value
      current = current.prev

      
if __name__ == "__main__":
  n1 = Node(41)
  n2 = Node(12)
  n3 = Node(13)
  n4 = Node(14)
  l = LinkedList()
  l.insert(n1)
  l.insert(n2)
  l.insert(n3)
  l.insert(n4)
  print l.size()
  l.delete(n2)
  l.print_list()
