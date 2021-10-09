
from timer import timeit
from string_reverse.string_reverse import *
from merge_sorted_arrays.merge_sorted_arrays import *
from linked_list.linked_list import LinkedList

@timeit
def main() -> None:
  myLinkedList = LinkedList(1)
  myLinkedList.insert(2, 1)
  myLinkedList.insert(3, 2)
  myLinkedList.insert("y", 1)
  print(myLinkedList) 

if __name__ == "__main__":
  print("Running...")
  main()


