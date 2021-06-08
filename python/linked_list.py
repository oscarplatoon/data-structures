class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self, head = None):
    self.head = head
    self.size = 0

  def get_size(self):
    return self.size

#Remove node from end
  #def pop(self, data):
    this_node = self.head
    prev_node = None
    while this_node:
      if this_node.get_data() == data:
        if prev_node:
          prev_node.set_next(this_node.get_next_node())
        else:
          self.head = this_node
        self.size -= 1
        return True
      else:
        prev_node = this_node
        this_node = this_node.get_next_node()   
    return False    

#Add node from end
  def push(self, data):
    new_node = Node(data, self.head)
    self.head = new_node
    self.size += 1 

  def remove(self, data):
    this_node = self.head
    prev_node = None
    while this_node:
      if this_node.get_data() == data:
        if prev_node:
          prev_node.set_next(this_node.get_next())
        else:
          self.head = this_node
        self.length -= 1
        return True
      else:
          prev_node = this_node
          this_node = this_node.get_next()
    return False


  def get(self, element_to_get):
    this_node = self.head
    while this_node:
      if this_node.get_data() == element_to_get:
        return element_to_get
      else:
        this_node = this_node.get_data()
    return None
    

# ----- Node ------

class Node:
  def __init__(self, data, next_node = None):
    self.data = data
    self.next_node = next_node
  def get_next_node(self):
    return self.next_node
  def set_next_node(self, next_node):
    self.next_node = next_node
  def get_data(self):
    return self.data
  def set_data(self, data):
    self.data = data



x = LinkList([1,2,3])
print(x.remove([1,2,3]))
