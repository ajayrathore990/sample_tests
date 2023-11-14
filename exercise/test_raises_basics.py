
mylist = [1,2,3,4,5]
d = {1:'a',2:'b'}
import unittest

class ExceptionTest(unittest.TestCase):
	def test_assert_raise(self):
		with self.assertRaises(IndexError):
			mylist[5]

	def test_assert_raise1(self):
		with self.assertRaises(TypeError):
			2+ "span"

	def test_assert_raise2(self):
		with self.assertRaises(KeyError):
			d[3]

