import unittest
import unittest.mock as mock
import average_scores

class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert average_scores.average() == 90
    def test_average_zeroes_input(self):
        with mock.patch('builtins.input', side_effect=[0,0,0]):
            assert average_scores.average() == 0
    def test_average_same_input(self):
        with mock.patch('builtins.input', side_effect=[10,10,10]):
            assert average_scores.average() == 10

if __name__ == '__main__':
    unittest.main()
