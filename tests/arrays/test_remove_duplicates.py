from arrays import remove_duplicates
import unittest


class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        solution = remove_duplicates.Solution()
        arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        count = solution.remove_duplicates(arr)
        self.assertEqual(count, 5)
        self.assertEqual(arr[:5], [0, 1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
