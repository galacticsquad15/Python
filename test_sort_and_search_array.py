import unittest
import array as arr
import sort_and_search_array


class MyTestCase(unittest.TestCase):
    def test_item_found(self):
        the_array = arr.array('I', [1, 2, 3, 4, 5])
        self.assertEqual(sort_and_search_array.search_array(1, the_array), "Found!")

    def test_item_not_found(self):
        the_array = arr.array('I', [1, 2, 3])
        self.assertEqual(sort_and_search_array.search_array(4, the_array), "Not found.")

    def test_sort(self):
        the_array = arr.array('I', [4, 3, 2, 1])
        self.assertEqual(sort_and_search_array.sort_array(the_array), [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
