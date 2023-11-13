
'''
sample doc test
'''


def first(a,b):
	"""
	>>> first(3,3)
	6
	>>> first(5,1)
	6
	"""
	return a+b



def sub(a,b):
	"""
	>>> sub(10,5)
	5
	"""
	return a-b


def squar(a):
	"""
	>>> squar(4)
	16

	>>> squar(5)
	25
	"""
	return a**2


def type_check(a):
	"""
	>>> type_check('a')
	<class 'str'>

	>> type_check('34')
	<class 'int'>

	>>> type_check([1,2,3,4,5])
	<class 'list'>

	>>> type_check((1,2,3,4,5))
	<class 'tuple'>
	"""

	return type(a)

#python -m doctest  doc.py
#python -m doctest  -v doc.py
