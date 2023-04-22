# Corbyn Eaker
# M05 test.py
# This app tests that the results in the two functions are what we expect them to be

# imports
from fractions import Fraction
import unittest
from my_sum import sum

# class that will hold the two functions being tested
class TestSum(unittest.TestCase):
    # function to sum the integers in a list and check to see if the result is what we expect it to be (in this case 6)
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
    # function to sum fractions and see if the sum if what we expect it to be (this on is intentionally incorrect to see the error message)
    def test_list_fraction(self):
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()

# The assert test is a way to tell the program what the value should be and it'll raise an error if it isn't that assertion
# The result of the first test