
class Node:
    """
    Initialize a node with only next and value
    """
    def __init__(self, value):
      self.value = value
      self.next = None

class Stack:
    """
    Stack ADT implimentation
    """
    def __init__(self):
      self.head = Node("head")
      self.size = 0


    # return the items in stack in a more readable format
    def __str__(self):
      curr = self.head.next
      ret = ""
      while curr:
         ret += str(curr.value) + "->"
         curr = curr.next
      return ret[:-3]

    # count total items
    def getlength(self):
      return self.size


    # check if Empty
    def isEmpty(self):
      return self.size == 0


    # returns the last / top elemetn from the adt
    def peek(self):
       # check first if empty
      if self.isEmpty():
         raise Exception("the ADt has no data currently")
      return self.head.next.value


    # insert a value to the ADT
    def push(self, value):
      node = Node(value)
      node.next = self.head.next
      self.head.next = node
      # increment the size of the stack
      self.size += 1



    # delete and return the last element in the statck
    def pop(self):
      if self.isEmpty():
         raise Exception("The ADT is currently Empty")
    # delete last Element
      rem = self.head.next
      self.head.next = self.head.next.next
      # decresse the count
      self.size -= 1
      return rem.value


stack = Stack()

for val in [3,6,2,56,8,34,465,23,23,2343]:
    stack.push(val)
print(stack.peek())
