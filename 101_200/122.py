import sys
sys.path.append('.')
from schema import time_it


class Solution:
    @time_it
    def maxProfit(self, prices: list) -> int:
        """O(N) Time, O(1) Space"""
        peak = 0
        valley = 0
        max_profit = 0
        while peak < len(prices) - 1 and valley < len(prices) - 1:
            while valley < len(prices) - 1 and prices[valley + 1] <= prices[valley]: 
                valley += 1
            peak = valley
            while peak < len(prices) - 1 and prices[peak + 1] >= prices[peak]:
                peak += 1
            max_profit += prices[peak] - prices[valley]
            valley = peak
        return max_profit

    @time_it
    def maxProfit2(self, prices: list) -> int:
        """O(N) Time, O(1) Space, but much more simpler"""
        max_profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                max_profit += prices[i + 1] - prices[i]
        return max_profit


solu = Solution()
prices = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]
assert solu.maxProfit(prices) == 7
assert solu.maxProfit(prices2) == 0

assert solu.maxProfit2(prices) == 7
assert solu.maxProfit2(prices2) == 0

"""
Output example:
[6.0800ms]maxProfit -> 7
[2.4440ms]maxProfit -> 0
[3.1740ms]maxProfit2 -> 7
[1.3220ms]maxProfit2 -> 0
"""
