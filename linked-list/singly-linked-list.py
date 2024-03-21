class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def print_list(self):
    cur_node = self.head
    print_value = ""
    while cur_node:
      print_value += str(cur_node.data) + ("" if cur_node.next == None else " -> ")
      cur_node = cur_node.next
    print(print_value)

  def append(self, data):
    new_node = Node(data)

    if self.head is None:
      self.head = new_node
      return 

    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node
  
  def prepend(self, data):
    new_node = Node(data)

    new_node.next = self.head
    self.head = new_node

  def insert_after_node(self, prev_node, data):
    if not prev_node:
      print("Previous node does not exist.")
      return
    if not isinstance(prev_node, Node):
      print("Previous node is not a Node object.")
      return

    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node


# Test
linked_list = LinkedList()
linked_list.append("A")
linked_list.append("B")
linked_list.append("C")
linked_list.append("D")

linked_list.insert_after_node(linked_list.head.next, "Y")

linked_list.prepend("Z")


linked_list.print_list() 