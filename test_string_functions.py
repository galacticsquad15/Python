import unittest
import string_functions


class MyTestCase(unittest.TestCase):
    def test_multiply_string(self):
        my_string = string_functions.multiply_string("Python", 2)
        self.assertEqual(my_string, "PythonPython")

    def test_multiply_string_again(self):
        my_string = string_functions.multiply_string("C++", 5)
        self.assertEqual(my_string, "C++C++C++C++C++")


if __name__ == '__main__':
    unittest.main()
