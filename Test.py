#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import summation

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [20, 30]
        result = summation(data)
        self.assertEqual(result, 500)

    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [20, 70]
        result = summation(data)
        self.assertEqual(result, 5005)
      
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [10, 30]
        result = summation(data)
        self.assertEqual(result, 40)
     
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [-1, 0, 1]
        result = summation(data)
        self.assertEqual(result, 0)
      
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [0, 1]
        result = summation(data)
        self.assertEqual(result, 1)
         

if __name__ == '__main__':
    unittest.main()
