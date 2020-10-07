from arrays import contains_duplicates
import unittest


class TestDuplicates(unittest.TestCase):
    def test_include_duplicates(self):
        solution = contains_duplicates.Solution()
        nums = [1, 4, 2, 1, 1, 6, 3, 4, 1]
        result = solution.contains_duplicate(nums)
        self.assertEqual(result, True)

    def test_exclude_duplicates(self):
        solution = contains_duplicates.Solution()
        nums = [1, 2, 10, 6, 4, 3]
        result = solution.contains_duplicate(nums)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
