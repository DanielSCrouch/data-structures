
from typing import List
from linked_list.linked_list import LinkedList

class Queue(object):

  def __init__(self) -> None:
    self.data = LinkedList()

  def enqueue(self, item: object) -> None:
    """Add item to end of queue"""
    if not item:
      raise ValueError("Item value of None provided")

    self.data.append(item)

  def dequeue(self) -> object:
    """Return and remove next item from queue. Returns None if empty"""
    if len(self.data) == 0:
      return None
    value = self.data.search(0)
    self.data.remove(0)
    return value

  def peek(self) -> object:
    """Returns next item from queue without removing item. Returns None if empty"""
    if len(self.data) == 0:
      return None
    return self.data.search(0)
    
  def __len__(self) -> int:
    """Return integer count of items currently in queue"""
    return len(self.data)
  
  def is_empty(self) -> bool:
    """Returns True if empty"""
    return len(self.data) == 0




