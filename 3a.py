'''
The Arrange step creates a variable named “negative” for testing.
The Act step calls the “abs” function using the “negative” variable 
and stores the returned value in a variable named “answer.”
The Assert step verifies that “answer” is a positive value.
'''
import unittest

class Test3a(unittest.TestCase):
    def test_abs_for_a_negative_number(self):
        # Arrange or setup
        negative = -5
  
        # Act or action 
        answer = abs(negative)
  
        # Assert
        assert answer == 5

