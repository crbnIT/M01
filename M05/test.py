# Corbyn Eaker
# test.py
# this program uses unittest to test different types of expected outputs 

# importing fractions, unittest and my_sum
from fractions import Fraction
import unittest
from my_sum import sum

# creating test class
class TestSum(unittest.TestCase):
    # functions to test a list of integers
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    # function to test list of fractions, intentionally failing
    def test_list_fraction(self):
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()