import unittest
import binary_search

class TestBinarySearch(unittest.TestCase):
    def binary_search_test(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_index = 8
        self.assertEqual(expected_index, binary_search.binary_search(arr, 9))


if __name__ == '__main__':
    unittest.main()