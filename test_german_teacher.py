import unittest
import GermanTeacher


class TestFunctions(unittest.TestCase):
    def test_check_username_input_with_valid_input(self):
        username = "Robert"
        self.assertEqual(GermanTeacher.check_username_input(username), "Robert")

    def test_check_to_learn_again_with_valid_argument(self):
        argument = 1
        self.assertEqual(GermanTeacher.check_to_learn_again(argument), '1')

    def test_check_to_learn_again_with_invalid_argument(self):
        argument = 2
        self.assertEqual(GermanTeacher.check_to_learn_again(argument), "On to the test!")

class TestOutputPoints(unittest.TestCase):
    def setUp(self):
        points = 5
        self.OutputPoints = GermanTeacher.OutputPoints(points)

    def tearDown(self):
        del self.OutputPoints

    def test_constructor(self):
        self.assertEqual(self.OutputPoints.total_points, 5)

    def test_display(self):
        self.assertEqual(self.OutputPoints.display(), "5 out of 5! Great job!")


if __name__ == '__main__':
    unittest.main()
