"""Implementation of single linked list.
   First create a node class with next field and value field."""

class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList(object):
  """Creates a linked list object with below methods for it"""
  def __init__(self, head=None):
    self.head = None

  def insertNode(self, node):
      if self.head:
        node.next = self.head
        # reset head to new node.
        self.head = node 
      else:
        self.head = node

  def print_linkedlist(self):
    """Print linked list values one by one."""

    t = self.head
    while t.next:
      print t.next.value
      t = t.next
  def size(self):
    """Find size of linked list."""

    t = self.head
    size = 0
    while t.next:
      size += 1
      t = t.next
    return "size: %s"%(size,)
    
  def delete_node(self):
    if self.size() == 0:
      raise ValueError("List is empty")
    else:
      current = self.head
      prev = None
      while not found:
        if current == node:
          found = True
        elif current is None:
          raise ValueError("Node not in Linked List")
        else:
          previous = current
          current = current.next
      if previous is None:
        self.head = current.next
      else:
        previous.next = current.next

  def search(self, node):
    if self.size() == 0:
      raise ValueError("No such node available.")
    elif self.head == node:
      return node.value
    else:
      current_node = self.head
      c = 1
      while current_node.next:
        if current_node.next == node:
          return "Found the node value %s in %s position" % (node.value, c)
        else:
          current_node = current_node.next
        c += 1
if __name__ == "__main__":
  l = LinkedList()
  n1 = Node(1)
  n2 = Node(2)
  n3 = Node(3)
  n4 = Node(4)
  l.insertNode(n1)
  l.insertNode(n2)
  l.insertNode(n3)
  l.insertNode(n4)
  #l.insertNode(Node(14))
  l.print_linkedlist()
  print l.size()
  print l.search(n1)
