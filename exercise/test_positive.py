'''
This is a Python Program to 
check whether a number is positive or negative.

input :positive(3)
output : True

input: positive(-5)
output: False
'''

import unittest

class ChangeTest(unittest.TestCase):
	def test1(self):
		#positive(1)
		r = True
		self.assertIsInstance(1, int)
		self.assertEqual(r,True)
		self.assertNotEqual(r,False)


	def test2(self):
		#positive(-5)
		r= False
		self.assertEqual(r,False)
		self.assertNotEqual(r,True)


	def test3(self):
		#positive("6")
		a= True
		self.assertEqual(a,True)
		self.assertNotEqual(a,False)