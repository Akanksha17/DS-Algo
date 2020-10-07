from arrays import max_profit
import unittest


class MaxProfit(unittest.TestCase):
    def test_max_profit(self):
        prices = [7, 3, 5, 1, 2, 4, 2]
        solution = max_profit.Solution()
        profit = solution.max_profit(prices)
        self.assertEqual(profit, 5)

    def test_zero_profit(self):
        prices = [7, 6, 5, 4, 3, 2, 1]
        solution = max_profit.Solution()
        profit = solution.max_profit(prices)
        self.assertEqual(profit, 0)


if __name__ == '__main__':
    unittest.main()
