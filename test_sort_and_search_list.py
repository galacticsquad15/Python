import unittest
import sort_and_search_list


class MyTestCase(unittest.TestCase):
    def test_search_list_not_found(self):
        the_list = [1, 2, 3, 4, 5]
        self.assertEqual(sort_and_search_list.search_list(6, the_list), "Not found.")

    def test_search_list_found(self):
        the_list = [1, 2, 3, 4, 5]
        self.assertEqual(sort_and_search_list.search_list(1, the_list), "Found!")

    def test_sort_list(self):
        the_list = [4, 3, 6, 1]
        self.assertEqual(sort_and_search_list.sort_list(the_list), [1, 3, 4, 6])


if __name__ == '__main__':
    unittest.main()
