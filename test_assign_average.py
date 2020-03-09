import unittest
import assign_average


class MyTestCase(unittest.TestCase):
    def test_a(self):
        my_value = 'A'
        self.assertEqual(assign_average.switch_average(my_value), 1)

    def test_b(self):
        my_value = 'B'
        self.assertEqual(assign_average.switch_average(my_value), 2)

    def test_c(self):
        my_value = 'C'
        self.assertEqual(assign_average.switch_average(my_value), 3)

    def test_d(self):
        my_value = 'D'
        self.assertEqual(assign_average.switch_average(my_value), 4)

    def test_e(self):
        my_value = 'E'
        self.assertEqual(assign_average.switch_average(my_value), 5)

    def test_incorrect_key(self):
        my_value = 'F'
        self.assertEqual(assign_average.switch_average(my_value), "Invalid entry")


if __name__ == '__main__':
    unittest.main()
