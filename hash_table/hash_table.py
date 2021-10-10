
from timer import timeit
from linked_list.linked_list import LinkedList
from typing import Union

class HashTable(object):

  def __init__(self, size: int) -> None:
    self.data = [None] * size

  def hash(self, s: str) -> int:
    # Validate string input 
    if type(s) not in (str, int, float, bool):
      raise TypeError(f'unhashable type: {type(s)}')
    s = str(s)

    # Calculate hashed index (mod of size)
    hash = 0
    for i in range(0, len(s), 1):
      hash = (hash + ord(s[i]) * (i + 1)) % len(self.data)

    return hash

  def insert(self, key: Union[str, int, float, bool], value: object) -> None:
    index = self.hash(key)
    if self.data[index] == None:
      self.data[index] = LinkedList()
    self.data[index].append([key, value]) 

  def search(self, key: Union[str, int, float, bool]) -> object:
    index = self.hash(key)
    ll = self.data[index]
    value = None
    if ll is not None: 
      for item in ll.traverse():
        if item[0] == key:
          value = item[1]
          break
    return value

  def delete(self, key: Union[str, int, float, bool]) -> None:
    index = self.hash(key)
    self.data[index] = None



