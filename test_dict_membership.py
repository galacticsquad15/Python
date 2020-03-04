import unittest
import dict_membership


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        my_dictionary = {1 : 100, 2 : 90, 3 : 50, 4 : 30}
        self.assertEqual(dict_membership.in_dict(1, my_dictionary), True)

    def test_in_dict_false(self):
        my_dictionary = {1 : 100, 2 : 90, 3 : 50, 4 : 30}
        self.assertEqual(dict_membership.in_dict(5, my_dictionary), False)


if __name__ == '__main__':
    unittest.main()
