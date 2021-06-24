# =================================================================================================
# HARD ==========================================================================================
# =================================================================================================


import unittest

class NameTest(unittest.TestCase):
    
    def test_hello_first(self):
        self.assertEqual("Hello" + " " + ("John"), "Hello John")

    def test_hello_last(self):
        self.assertEqual("Hello" + " " + ("John Doe"), "Hello John Doe")


class GetName(unittest.TestCase):
    
    # def test_first_upper(self):
    #     self.assert

    # def test_last_upper(self):
    #     self.assert

if __name__ == '__main__':
    unittest.main()