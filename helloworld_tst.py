import unittest

from helloworld import *

class TestCalc(unittest.TestCase):

  def test_hello(self):
    self.assertEqual(hello_world(1, 1), 2)
