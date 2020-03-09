import unittest
import assign_average


class MyTestCase(unittest.TestCase):
    def test_a(self):
        my_dict = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5}
        my_value = 'A'
        self.assertEqual(assign_average.switch_average(my_value, my_dict), True)

    def test_b(self):
        my_dict = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5}
        my_value = 'B'
        self.assertEqual(assign_average.switch_average(my_value, my_dict), True)

    def test_c(self):
        my_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
        my_value = 'C'
        self.assertEqual(assign_average.switch_average(my_value, my_dict), True)

    def test_d(self):
        my_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
        my_value = 'D'
        self.assertEqual(assign_average.switch_average(my_value, my_dict), True)

    def test_e(self):
        my_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
        my_value = 'E'
        self.assertEqual(assign_average.switch_average(my_value, my_dict), True)

    def incorrect_key(self):
        my_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
        my_value = 'F'
        self.assertEqual(assign_average.switch_average(my_value, my_dict), False)


if __name__ == '__main__':
    unittest.main()
