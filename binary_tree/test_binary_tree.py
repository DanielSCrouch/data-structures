import unittest
from binary_tree.binary_tree import BinaryTree, Node

class TestNode(unittest.TestCase):

  def test_node_value_error(self):
    self.assertRaises(ValueError, Node, None, None, None)
    self.assertRaises(ValueError, Node, "a", None, None)
    self.assertRaises(ValueError, Node, {}, None, None)

    self.assertRaises(ValueError, Node, 1, 1, None)
    self.assertRaises(ValueError, Node, 1, None, 1)

  def test_create_node(self):
    self.assertIsInstance(Node(1, None, None), Node) 

  def test_print_node(self):
    root = Node(4, None, None)
    root.set_left_node(Node(2, Node(1, None, None), Node(3, None, None))) 
    root.set_right_node(Node(6, Node(5, None, None), Node(7, None, None)))  
    self.assertEqual(root.__str__(), "1, 2, 3, 4, 5, 6, 7")

class TestBinaryTree(unittest.TestCase):

  def test_search_empty(self):
    bt = BinaryTree() 
    self.assertEqual(bt.search(1), False)

  def test_create_simple_tree1(self):
    bt = BinaryTree()
    bt.insert(1) 
    self.assertEqual(bt.root.value, 1)

  def test_create_simple_tree2(self):
    bt = BinaryTree()
    bt.insert(1)
    bt.insert(2) 
    self.assertEqual(bt.root.value, 1)
    self.assertEqual(bt.root.right.value, 2)

  def test_create_simple_tree3(self):
    bt = BinaryTree()
    bt.insert(15)
    bt.insert(6)
    bt.insert(4)
    bt.insert(5)
    bt.insert(7)
    bt.insert(23)
    bt.insert(71)
    bt.insert(50)

    self.assertEqual(bt.root.value, 15)
    self.assertEqual(bt.root.left.value, 6)
    self.assertEqual(bt.root.left.left.value, 4) 
    self.assertEqual(bt.root.left.left.right.value, 5) 
    self.assertEqual(bt.root.left.right.value, 7) 
    self.assertEqual(bt.root.right.value, 23) 
    self.assertEqual(bt.root.right.right.value, 71) 
    self.assertEqual(bt.root.right.right.left.value, 50)

  def test_remove_edge(self):
    bt = BinaryTree()
    bt.insert(15)
    bt.insert(6)
    bt.insert(4)
    bt.insert(5)
    bt.insert(7)
    bt.insert(23)
    bt.insert(71)
    bt.insert(50)

    bt.remove(5)

    self.assertEqual(bt.root.value, 15)
    self.assertEqual(bt.root.left.value, 6)
    self.assertEqual(bt.root.left.left.value, 4) 
    self.assertEqual(bt.root.left.left.right, None) 
    self.assertEqual(bt.root.left.right.value, 7) 
    self.assertEqual(bt.root.right.value, 23) 
    self.assertEqual(bt.root.right.right.value, 71) 
    self.assertEqual(bt.root.right.right.left.value, 50)

    bt.remove(7)

    self.assertEqual(bt.root.value, 15)
    self.assertEqual(bt.root.left.value, 6)
    self.assertEqual(bt.root.left.left.value, 4) 
    self.assertEqual(bt.root.left.left.right, None) 
    self.assertEqual(bt.root.left.right, None) 
    self.assertEqual(bt.root.right.value, 23) 
    self.assertEqual(bt.root.right.right.value, 71) 
    self.assertEqual(bt.root.right.right.left.value, 50)

    bt.remove(4)

    self.assertEqual(bt.root.value, 15)
    self.assertEqual(bt.root.left.value, 6)
    self.assertEqual(bt.root.left.left, None) 
    self.assertEqual(bt.root.left.right, None) 
    self.assertEqual(bt.root.right.value, 23) 
    self.assertEqual(bt.root.right.right.value, 71) 
    self.assertEqual(bt.root.right.right.left.value, 50)

  def test_remove_left_node(self):
    bt = BinaryTree()
    bt.insert(15)
    bt.insert(6)
    bt.insert(4)
    bt.insert(5)
    bt.insert(7)
    bt.insert(23)
    bt.insert(71)
    bt.insert(50)

    bt.remove(6)

    self.assertEqual(bt.root.value, 15)
    self.assertEqual(bt.root.left.value, 7)
    self.assertEqual(bt.root.left.left.value, 4) 
    self.assertEqual(bt.root.left.left.right.value, 5) 
    self.assertEqual(bt.root.left.right, None) 
    self.assertEqual(bt.root.right.value, 23) 
    self.assertEqual(bt.root.right.right.value, 71) 
    self.assertEqual(bt.root.right.right.left.value, 50)

  def test_remove_right_node(self):
    bt = BinaryTree()
    bt.insert(15)
    bt.insert(6)
    bt.insert(4)
    bt.insert(5)
    bt.insert(7)
    bt.insert(23)
    bt.insert(71)
    bt.insert(50)

    bt.remove(71)

    self.assertEqual(bt.root.value, 15)
    self.assertEqual(bt.root.left.value, 6)
    self.assertEqual(bt.root.left.left.value, 4) 
    self.assertEqual(bt.root.left.left.right.value, 5) 
    self.assertEqual(bt.root.left.right.value, 7) 
    self.assertEqual(bt.root.right.value, 23) 
    self.assertEqual(bt.root.right.right.value, 50) 


  def test_remove_right_node2(self):
    bt = BinaryTree()
    bt.insert(15)
    bt.insert(6)
    bt.insert(4)
    bt.insert(5)
    bt.insert(7)
    bt.insert(23)
    bt.insert(71)
    bt.insert(50)
    bt.insert(55)
    bt.insert(75)

    bt.remove(71)

    self.assertEqual(bt.root.value, 15)
    self.assertEqual(bt.root.left.value, 6)
    self.assertEqual(bt.root.left.left.value, 4) 
    self.assertEqual(bt.root.left.left.right.value, 5) 
    self.assertEqual(bt.root.left.right.value, 7) 
    self.assertEqual(bt.root.right.value, 23) 
    self.assertEqual(bt.root.right.right.value, 50)
    self.assertEqual(bt.root.right.right.right.value, 55)
    self.assertEqual(bt.root.right.right.right.right.value, 75) 
    
    