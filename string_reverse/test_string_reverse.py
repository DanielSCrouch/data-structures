import unittest
from timer import timeit

from string_reverse.string_reverse import *


class TestStringReverse(unittest.TestCase):

  @timeit
  def test_reverse1(self):
    self.assertEqual(reverse1("abc"), "cba") 
    self.assertEqual(reverse1("abcdefghijklmnop"), "ponmlkjihgfedcba") 
    self.assertEqual(reverse1("abcdefghijklmnopz"), "zponmlkjihgfedcba") 

  @timeit
  def test_reverse2(self):
    self.assertEqual(reverse2("abc"), "cba") 
    self.assertEqual(reverse2("abcdefghijklmnop"), "ponmlkjihgfedcba") 
    self.assertEqual(reverse2("abcdefghijklmnopz"), "zponmlkjihgfedcba") 

  @timeit
  def test_reverse3(self):
    self.assertEqual(reverse3("abc"), "cba") 
    self.assertEqual(reverse3("abcdefghijklmnop"), "ponmlkjihgfedcba") 
    self.assertEqual(reverse3("abcdefghijklmnopz"), "zponmlkjihgfedcba") 

  @timeit
  def test_recursive_reverse(self):
    self.assertEqual(reverse4("abc"), "cba") 
    self.assertEqual(reverse4("abcdefghijklmnop"), "ponmlkjihgfedcba") 
    self.assertEqual(reverse4("abcdefghijklmnopz"), "zponmlkjihgfedcba") 



