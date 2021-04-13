# =================================================================================================
# HARD ==========================================================================================
# =================================================================================================


import unittest
from Code_Review_Apr_15 import name

class NameTest(unittest, TestCase):
    
    def test_hello_first(self):
        self.assertEqual(Hello("John"), "Hello John")

    def test_hello_last(self):
        self.assertEqual(Hello("John Doe"), "Hello John Doe")

    def test_hello_is_not_integer(self):
        self.assertIsNot(int("John", 9))

if __name__ == '__main__':
    unittest.main()
