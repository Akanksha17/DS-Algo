from search_algos.binary_search import binary_search
import unittest


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_num_present(self):
        nums = [1, 4, 8, 8, 9, 11, 23, 25, 31]
        num = 23
        idx = binary_search(nums, 0, len(nums), num)
        self.assertEqual(idx, 6)

    def test_binary_search_num_absent(self):
        nums = [1, 4, 8, 8, 9, 11, 23, 25, 31]
        num = 20
        idx = binary_search(nums, 0, len(nums), num)
        self.assertEqual(idx, -1)


if __name__ == '__main__':
    unittest.main()
