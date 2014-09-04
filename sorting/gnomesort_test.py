import unittest
import gnomesort
class TestGnomesort(unittest.TestCase):
    def test_sort(self):
        seq = [2, 1, 10, 8, 4, 3, 5, 6, 9, 7]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(expected_result, gnomesort.gnomesort(seq))


if __name__ == '__main__':
    unittest.main()
