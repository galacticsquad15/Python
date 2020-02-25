import unittest
import validate_input_in_functions


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        testName = validate_input_in_functions.score_input('Python Test')
        self.assertEqual('Python Test', testName)

    def test_score_input_test_score_valid(self):
        testName = validate_input_in_functions.score_input('Python Test', 90)
        self.assertEqual('Python Test: 90', testName)

    def test_score_input_test_score_below_range(self):
        testName = validate_input_in_functions.score_input('Python Test', -1)
        self.assertEqual('Invalid test score, try again!', testName)

    def test_score_input_test_score_above_range(self):
        testName = validate_input_in_functions.score_input('Python Test', 101)
        self.assertEqual('Invalid test score, try again!', testName)

    def test_test_score_non_numeric(self):
        testName = validate_input_in_functions.score_input('Python Test', '!')
        self.assertEqual('Invalid test score, try again!', testName)

    def test_score_input_invalid_message(self):
        testName = validate_input_in_functions.score_input('Python Test', 101, 'Try Again.')
        self.assertEqual('Try Again.', testName)


if __name__ == '__main__':
    unittest.main()
