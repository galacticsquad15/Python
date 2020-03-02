import unittest
from unittest.mock import patch
import basic_list as topic1


class MyTestCase(unittest.TestCase):
    @patch('basic_list.get_input', return_value = '4')
    def test_make_list(self, input):
        self.assertEqual(topic1.make_list(), [4, 4, 4])


if __name__ == '__main__':
    unittest.main()
