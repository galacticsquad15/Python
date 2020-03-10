import unittest
import half_birthday
import datetime


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        my_birthday = datetime.datetime(1994, 5, 3)
        self.assertEqual(half_birthday.my_half_birthday(my_birthday), datetime.datetime(1994, 11, 2, 0, 0))


if __name__ == '__main__':
    unittest.main()
