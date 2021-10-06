
from typing import List

class Stack(object):

  def __init__(self) -> None:
    self.data = [] 
    self.size = 0

  def push(self, item: object) -> None:
    """Add item to top of stack"""
    if not item:
      raise ValueError("Item value of None provided")

    self.data.append(item)
    self.size += 1 

  def pop(self) -> object:
    """Return and remove top item from stack. Returns None if empty"""
    if self.size == 0:
      return None
    
    self.size -= 1
    return self.data.pop(self.size)

  def peek(self) -> object:
    """Return top item from stack without removing item. Returns None if empty"""
    if self.size == 0:
      return None
    
    return self.data[self.size - 1]
    
  def size(self) -> int:
    """Return integer count of items currently in stack"""
    return self.size


