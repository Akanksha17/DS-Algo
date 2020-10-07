from arrays import single_number
import unittest


class Solution(unittest.TestCase):
    def test_single_number(self):
        solution = single_number.Solution()
        arr = [2, 2, 1]
        result = solution.single_number(arr)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
