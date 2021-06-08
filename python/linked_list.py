class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
    def __init__(self, head=None):
        self.head = head
    #   self.length

    def add(self, data):
        # write your code to ADD an element to the Linked List
        new_node = Node(data)
        # self.head = new_node

        if self.head is None:
            self.head = new_node
            return
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node
        return new_node
    

    def remove(self, data):
    # write your code to REMOVE an element from the Linked List
        current_node = self.head
        previous_node = None
        if current_node.data == data:
            # Assign new head to head's next -> node
            self.head = current_node.next_node
        else:
            while current_node.data != data:
            # Traversing the linked list
                previous_node = current_node
                current_node = current_node.next_node
            previous_node.next_node = current_node.next_node
        return self.head
            
    def get(self, element_to_get):
    # write you code to GET and return an element from the Linked List
        current_node = self.head
        print('element to get', element_to_get)
        index = 0
        while current_node.data != element_to_get:
            # Traversing the linked list
            # previous_node = current_node
            print('current:', current_node.data)
            current_node = current_node.next_node
            index += 1
            print('next node', current_node.next_node)
            if current_node.next_node:
                return 'element not found'
        return print('index', index)
                # return current_node.data   

    def print(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next_node 


# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  def __init__(self, data=None, next_node=None):
      self.data = data
      self.next_node  = next_node

# llist = LinkList()
# llist.add(3)
# llist.add(2)
# llist.add(1)
# print(llist.get(2))
