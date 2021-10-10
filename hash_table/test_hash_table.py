from typing import Type
import unittest
from hash_table.hash_table import HashTable
from linked_list.linked_list import LinkedList

class TestHashTable(unittest.TestCase):

  def test_create_table(self):
    ht = HashTable(3)
    
  def test_hash(self):
    ht = HashTable(3) 
    self.assertEqual(ht.hash("march 6"), 1) 
    self.assertEqual(ht.hash("abc"), 2) 

  def test_hash_type_error(self):
    ht = HashTable(3) 
    self.assertRaises(TypeError, ht.hash, {})
    self.assertRaises(TypeError, ht.hash, [])
    
  
  def test_insert(self):
    ht = HashTable(3) 
    ht.insert("a", 1)
    ht.insert("b", 2)
    ht.insert("b", 3)

  def test_search(self):
    ht = HashTable(10) 
    ht.insert("a", 1)
    ht.insert("b", 2)
    ht.insert("b", 3)

    self.assertEqual(ht.search("z1"), None)
    self.assertEqual(ht.search("a"), 1)
    self.assertEqual(ht.search("b"), 2)










