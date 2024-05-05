class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
  def __init__(self, head:LinkedListNode =None):
    self.head = head
    
  def insert(self, value: int):
    #  the next value of the node should be the head
    new_node = LinkedListNode(value)
    # and the head becomes the next
    new_node.next = self.head
    # and the head is now the new node
    self.head = new_node
    
  def print_list(self):
    if not self.head:
      print("The list is empty")
      return
    # starting from the head
    # we will print the value of all the nodes
    current_node = self.head
    while current_node:
      print(current_node.value)
      current_node = current_node.next
      
  def delete_head(self):
    #  if the list is empty warn the user
    if not self.head:
      print("List Empty")
      return
    else:
      self.head = self.head.next
    
    
        
        
root_node = LinkedListNode(1)

linked_list = LinkedList()
linked_list.print_list()

linked_list.insert(2)

linked_list.insert(22)

linked_list.insert(222)

linked_list.print_list()

linked_list.delete_head()

print("last print sta")
linked_list.print_list()

