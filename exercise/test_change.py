'''
This is a Python Program to exchange 
the values of two numbers without using a temporary variable.

# change(a,b)
# return b ,a
'''

import unittest


class ChangeTest(unittest.TestCase):
	def test1(self):
		a = 1,2
		self.assertEqual(a,(1,2))

	def test2(self):
		a= 4,5
		self.assertEqual(a,(4,5))

	def test3(self):
		a= 10,20
		self.assertEqual(a,(10,20))
		self.assertNotEqual(a,(20,10))


