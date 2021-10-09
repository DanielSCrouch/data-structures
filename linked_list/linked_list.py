
from typing import Iterator
from timer import timeit
from copy import deepcopy

@timeit
def reverse1(s: str) -> str:
  rl = []
  for e in s:
    rl = [e] + rl
  return "".join(rl)
  

class Node(object):

  def __init__(self, value: object, next: object) -> None:
    self.value = value
    self.next = next

  def __str__(self) -> None:
    return f'Node: [value: {self.value} \t next: {self.next.__repr__()}]'

class LinkedList(object):
  
  def __init__(self) -> None:
    self.head = None
    self.tail = self.head
    self.length = 0

  def prepend(self, value: object) -> None:
    """Add value to head of Linked List."""
    self.head = Node(value, self.head)
    self.length += 1

    # Set tail if first item
    if self.length == 1:
      self.tail = self.head

  def append(self, value: object) -> None:
    """Add value to tail of Linked List."""
    if not self.head:
      self.prepend(value)
      return

    self.tail.next = Node(value, None)
    self.tail = self.tail.next
    self.length += 1

  def traverse_to_index(self, index: int) -> Node:
    """Returns the node at the index position"""
    # Check index range
    if not index < self.length:
      raise ValueError(f'Index {index} out of LinkedList range 0-{self.length - 1}.')

    counter = 0
    node = self.head 
    while counter != index:
      node = node.next
      counter += 1
    return node

  def traverse(self) -> Iterator:
    """Returns a generator function returning all values in series"""
    node = self.head
    if node == None:
      yield None
    yield node.value
    while node.next:
      node = node.next
      yield node.value

  def insert(self, index: int, value: object) -> None:
    """Insert an item into the list at the index position"""
    # Check index range
    if not index < self.length:
      raise ValueError(f'Index {index} out of LinkedList range 0-{self.length - 1}.')

    # Insert at head
    if index == 0:
      self.prepend(value)
      return
    
    # Insert at midpoint
    lead_node = self.traverse_to_index(index - 1)
    lead_node.next = Node(value, lead_node.next)    
    self.length += 1

  def update(self, index: int, value: object) -> None:
    """Update value of node at index position"""
    node = self.traverse_to_index(index) 
    node.value = value

  def search(self, index: int) -> object:
    """Returns value at given index"""
    node = self.traverse_to_index(index)
    return node.value

  def remove(self, index: int) -> None:
    """Remove a value at the index position from the Linked List"""
    # Check index range
    if not index < self.length:
      raise ValueError(f'Index {index} out of LinkedList range 0-{self.length - 1}.')
    
    # Remove head
    if index == 0:
      self.head = self.head.next
      self.length -= 1
      return

    # Remove at index
    lead_node = self.traverse_to_index(index - 1)

    if lead_node.next:
      # next node skips over deleted
      lead_node.next = lead_node.next.next
    else:
      # handle tail node
      lead_node.next = None
      self.tail = lead_node
    self.length -= 1

  def reverse(self) -> None:
    """Reverses the serial order of the Linked List"""

    lead_node = self.head
    node = lead_node.next

    # Reverse head and tail
    self.head.next = None
    new_tail = self.head
    self.head = self.tail
    self.tail = new_tail

    while node:
      # Flip next node referece, then traverse one
      next_node = node.next
      node.next = lead_node
      lead_node = node
      node = next_node

  def deep_copy(self) -> object:
    """Returns deep copy of Linked List"""
    counter = 0
    node = self.head
    new_ll = LinkedList()
    while counter != self.length:
      if node:
        new_ll.append(deepcopy(node.value)) 
      node = node.next
      counter += 1 
    
    return new_ll

  def __eq__(self, o: object) -> bool:
      if not type(self) == type(o):
        return False

      if not self.length == o.length:
        return False

      traverse1 = self.traverse()
      traverse2 = o.traverse()
      for _ in range(self.length):
        value1 = traverse1.__next__()
        value2 = traverse2.__next__()
        if value1 != value2:
          return False
      
      return True

  def __str__(self):
    s = "Start"
    node = self.head 
    for _ in range(self.length):
      s += f'\n\tvalue: {node.value} \tnext: {node.next}'
      node = node.next
    s += "\nEnd" 

    return s

  def __len__(self) -> int:
    return self.length



  