import unittest
import string_functions


class MyTestCase(unittest.TestCase):
    def test_multiple_strings(self):
        my_string = string_functions.multiply_string("Python", 2)
        self.assertEqual(my_string, "PythonPython")


if __name__ == '__main__':
    unittest.main()
