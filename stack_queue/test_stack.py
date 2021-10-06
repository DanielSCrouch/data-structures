import unittest

from stack_queue.stack import *
from stack_queue.queue import *


class TestStack(unittest.TestCase):

  item1 = 1 
  item2 = "2"
  item3 = [3]

  ### Stack #######################################
    
  def test_push_stack(self):
    stack = Stack()
    
    stack.push(self.item1) 
    stack.push(self.item2) 
    stack.push(self.item3)

    self.assertEqual(stack.size, 3) 
    self.assertRaises(ValueError, stack.push, None) 

  def test_pop_stack(self):
    stack = Stack()
    stack.push(self.item1) 
    stack.push(self.item2) 
    stack.push(self.item3)

    self.assertEqual(stack.pop(), self.item3) 
    self.assertEqual(stack.size, 2) 
    self.assertEqual(stack.pop(), self.item2) 
    self.assertEqual(stack.size, 1) 
    self.assertEqual(stack.pop(), self.item1) 
    self.assertEqual(stack.size, 0)
    self.assertEqual(stack.pop(), None) 
    self.assertEqual(stack.size, 0)

  def test_peek_stack(self):
    stack = Stack()

    self.assertEqual(stack.peek(), None)

    stack.push(self.item1) 
    stack.push(self.item2) 
    stack.push(self.item3)

    self.assertEqual(stack.peek(), self.item3) 
    self.assertEqual(stack.size, 3) 
    self.assertEqual(stack.peek(), self.item3) 
    self.assertEqual(stack.size, 3) 
    self.assertEqual(stack.pop(), self.item3) 
    self.assertEqual(stack.size, 2)
    self.assertEqual(stack.peek(), self.item2) 
    self.assertEqual(stack.size, 2)

  ### Queue #######################################

  def test_enqueue_queue(self):
    queue = Queue()
    
    queue.enqueue(self.item1) 
    queue.enqueue(self.item2) 
    queue.enqueue(self.item3)

    self.assertEqual(len(queue), 3) 
    self.assertRaises(ValueError, queue.enqueue, None) 

  def test_dequeue_queue(self):
    queue = Queue()
    queue.enqueue(self.item1) 
    queue.enqueue(self.item2) 
    queue.enqueue(self.item3)

    self.assertEqual(queue.dequeue(), self.item1) 
    self.assertEqual(len(queue), 2) 
    self.assertEqual(queue.dequeue(), self.item2) 
    self.assertEqual(len(queue), 1) 
    self.assertEqual(queue.dequeue(), self.item3) 
    self.assertEqual(len(queue), 0)
    self.assertEqual(queue.dequeue(), None) 
    self.assertEqual(len(queue), 0)

  def test_peek_queue(self):
    queue = Queue()

    self.assertEqual(queue.peek(), None)

    queue.enqueue(self.item1) 
    queue.enqueue(self.item2) 
    queue.enqueue(self.item3)

    self.assertEqual(queue.peek(), self.item1) 
    self.assertEqual(len(queue), 3) 
    self.assertEqual(queue.peek(), self.item1) 
    self.assertEqual(len(queue), 3) 
    self.assertEqual(queue.dequeue(), self.item1) 
    self.assertEqual(len(queue), 2)
    self.assertEqual(queue.peek(), self.item2) 
    self.assertEqual(len(queue), 2)

  





