from arrays import plus_one
import unittest


class TestPlusOne(unittest.TestCase):
    def test_plus_one(self):
        nums = [2, 4, 5]
        solution = plus_one.Solution()
        result = solution.plus_one(nums)
        self.assertEqual(result, [2, 4, 6])


if __name__ == '__main__':
    unittest.main()