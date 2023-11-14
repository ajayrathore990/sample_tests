import unittest

class FirstTest(unittest.TestCase):
	def assert_true(self):
		assert True

	def test_assert_false(self):
		assert not False

	def test_assert_equal(self):
		assert  2+2 ==4

	def test_assert_not_equal(self):
		assert 2+2 != 5

	def test_assert_grater(self):
		assert  10 > 4

	def test_assert_less(self):
		assert 5 < 10


class SecondTest(unittest.TestCase):
	def test_self_equal(self):
		self.assertEqual(True, True)

	def test_self_not_equel(self):
		self.assertNotEqual(False,True)

	def test_self_equal_sum(self):
		self.assertEqual(2+2,4)

	def test_self_not_equal_sum(self):
		self.assertNotEqual(2+2, 5)


class ThirdTest(unittest.TestCase):
	def test_integer_instanse(self):
		self.assertIsInstance(1, int)

	def test_string_instanse(self):
		self.assertIsInstance('a',str)

	def test_list_instanse(self):
		self.assertIsInstance([1,2,3],list)

	def test_tupel_instase(self):
		self.assertIsInstance((1,2,3),tuple)

class FourthTest(unittest.TestCase):
	def test_grater_equal(self):
		self.assertGreaterEqual(10,5)

	def test_less_equal(self):
		self.assertLessEqual(5,10)

	def test_grater_or_equal(self):
		self.assertGreaterEqual(10,10)

	def test_less_or_equal(self):
		self.assertLessEqual(10,10)


class FifthTest(unittest.TestCase):
	def test_assert_raise0(self):
		with self.assertRaises(ZeroDivisionError):
			10/0

#python -m  unittest test_unit_basics.py
#python -m  unittest  -v test_unit_basics.py

