# from python.bst import Node


class LinkedList(object):
  def __init__(self, head=None):
    self.head = head
    # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList

  def size(self):
    if self.head == None:
      return 0
    current = self.head
    count = 0
    while current != None:
        count += 1
        current = self.next_node
    print(count)
# write your code to ADD an element to the Linked List
 # write your code to REMOVE an element from the Linked List



# ----- Node ------
  class Node:
  # store your DATA and NEXT values here
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


test = LinkedList([1])
print(test)