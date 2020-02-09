import unittest
import validation_with_try


class MyTestCase(unittest.TestCase):
    def test_average_negative_input_first_input(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(-1, 20, 90)

    def test_average_negative_input_second_input(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(1, -20, 90)

    def test_average_negative_input_third_input(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(1, 2, -3)


if __name__ == '__main__':
    unittest.main()
