import unittest

from linked_list.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

  def test_append(self):
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    
    self.assertEqual(ll.head.value, 1) 
    self.assertEqual(ll.head.next.value, 2) 
    self.assertEqual(ll.head.next.next.value, 3) 

  def test_insert(self):
    ll = LinkedList() 
    ll.append(1)
    ll.append(2)
    ll.append(3)

    ll.insert(0, "x")
    ll.insert(2, "y") 
    ll.insert(4, "z") 
    
    self.assertEqual(ll.head.value, "x") 
    self.assertEqual(ll.head.next.value, 1) 
    self.assertEqual(ll.head.next.next.next.value, 2) 
    self.assertEqual(ll.head.next.next.next.next.value, "z") 
    self.assertEqual(ll.head.next.next.next.next.next.value, 3) 

    self.assertEqual(ll.length, 6) 

    self.assertRaises(ValueError, ll.insert, 6, "a")

  def test_remove_head(self):
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    ll.remove(0) 

    self.assertEqual(ll.length, 2)
    self.assertEqual(ll.head.value, 2) 
    self.assertEqual(ll.head.next.value, 3) 

  def test_remove(self):
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    ll.remove(1) 

    self.assertEqual(ll.length, 2)
    self.assertEqual(ll.head.value, 1) 
    self.assertEqual(ll.head.next.value, 3) 
    self.assertEqual(ll.tail.value, 3) 

  def test_traverse(self):
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    traverse = ll.traverse()
    self.assertEqual(traverse.__next__(), 1)
    self.assertEqual(traverse.__next__(), 2)
    self.assertEqual(traverse.__next__(), 3)

  def test_search(self):
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    self.assertEqual(ll.search(1), 2) 

  def test_reverse(self):
    ll = LinkedList() 
    ll.append(1) 
    ll.append(2)
    ll.append(3)

    ll.reverse()
    traverse = ll.traverse()
    self.assertEqual(traverse.__next__(), 3)
    self.assertEqual(traverse.__next__(), 2)
    self.assertEqual(traverse.__next__(), 1)

  def test_update(self):
    ll = LinkedList()  
    ll.append(1)
    ll.append(2)
    ll.append(3)

    ll.update(1, "x") 

    traverse = ll.traverse()
    self.assertEqual(traverse.__next__(), 1)
    self.assertEqual(traverse.__next__(), "x")
    self.assertEqual(traverse.__next__(), 3)


  def test_deep_copy(self):
    ll = LinkedList()  
    ll.append(1)
    ll.append(2)
    ll.append(3)

    ll2 = ll.deep_copy()

    self.assertEqual(ll.length, ll2.length)

    ll.update(1, "x") 

    self.assertEqual(ll2.search(1), 2) 

  def test_deep_copy2(self):
    ll = LinkedList()  
    ll.append(1)
    ll.append(["a", "b", "c"])
    ll.append(3)

    ll2 = ll.deep_copy()

    self.assertEqual(ll.length, ll2.length)

    ll.search(1)[1] = "x"

    self.assertEqual(ll2.search(1), ["a", "b", "c"]) 

  def test_equal(self):
    ll = LinkedList()  
    ll.append(1)
    ll.append(2)
    ll.append(3)

    ll2 = ll.deep_copy()

    self.assertEqual(ll == ll2, True)

    ll.update(1, 3) 

    self.assertEqual(ll == ll2, False)

    



