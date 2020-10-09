from arrays import move_zeroes
import unittest


class TestMoveZeroes(unittest.TestCase):
    def test_plus_one(self):
        nums = [1, 0, 0, 3, 4, 1, 0, 0]
        solution = move_zeroes.Solution()
        result = solution.move_zeroes(nums)
        self.assertEqual(result, [1, 3, 4, 1, 0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()