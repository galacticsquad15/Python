"""
Write a test test_in_set_true
assertion for an item in the set (expect True)
Write a test test_in_set_false
One assertion for an item not in the set (expect False)
Run the test, see it fail, commit to github
Write the in_set function.
Run the test, see it pass, commit to github.
"""
import unittest
import set_membership


class MyTestCase(unittest.TestCase):
    def test_in_set_false(self):
        my_set = {1, 2, 3, 4, 5}
        self.assertEqual(set_membership.in_set(6, my_set), False)


if __name__ == '__main__':
    unittest.main()
