'''
This is a Python Program to reverse a given number.

revers(123)
321

'''
import unittest


class ChangeTest(unittest.TestCase):
	def test1(self):
		#revers("ajay")
		r = 'yaja'
		self.assertEqual(r,'yaja')

	def test2(self):
		#revers('str')
		r= 'rts'
		self.assertEqual(r,'rts')

	def test3(self):
		#revers("01")
		a= 10
		self.assertEqual(a,10)
		self.assertNotEqual(a,20)


