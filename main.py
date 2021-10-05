
from timer import timeit
from string_reverse.string_reverse import *
from merge_sorted_arrays.merge_sorted_arrays import *
# from hash.hash import *
from linked_list.linked_list import LinkedList

def main() -> None:
  
  # a = "abcdefghijklmnopqrstuvwxyz" * 1000

  # reverse1(a)
  # reverse2(a)
  # reverse3(a)

  # a = [0, 3, 4, 31] * 1000
  # a.sort()
  # b = [4, 6, 30] * 1000
  # b.sort()

  # merge_sorted_arrays1(a, b)
  # merge_sorted_arrays2(a, b)
  # merge_sorted_arrays3(a, b)

  # myHashTable = HashTable(10)

  myLinkedList = LinkedList(1)
  myLinkedList.insert(2, 1)
  myLinkedList.insert(3, 2)
  # myLinkedList.insert("x", 2)
  myLinkedList.insert("y", 1)
  print(myLinkedList) 







if __name__ == "__main__":
  print("Running...")
  main()


