"""
Best Time To Buy And Sell Stock Series
"""

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'

import sys
sys.path.append('.')
from schema import time_it


class Solution:
    """
    121. Best Time To Buy And Sell Stock 买卖股票的最佳时机
    Difficulty: Easy
    Description: 只允许完成一笔交易，即买入和卖出一支股票
    """

    @classmethod
    @time_it
    def brute_force(self, prices: list) -> int:
        '''brute force
        Time: O(N^2)
        Space: O(1)
        '''
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit

    @classmethod
    @time_it
    def one_traversal(self, prices: list) -> int:
        '''find valley and peek
        Time: O(N)
        Space: O(1)
        '''
        min_price = float("Inf")
        max_profit = 0
        for item in prices:
            if item < min_price:
                min_price = item
            else:
                max_profit = max(max_profit, item-min_price)
        return max_profit

case1 = [7, 1, 5, 3, 6, 4]
case2 = [7, 6, 5, 4, 3, 2, 1]
assert Solution.brute_force(case1) == 5
assert Solution.brute_force(case2) == 0
assert Solution.one_traversal(case1) == 5
assert Solution.one_traversal(case2) == 0


class Two:
    """
    122. Best Time To Buy And Sell A Stock II 买卖股票的最佳时机2
    Difficulty: Easy
    Description: 能参与多次交易，但是必须在购买前出售掉之前的股票
    """

    @classmethod
    @time_it
    def maxProfit(self, prices) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            profit = prices[i+1] - prices[i]
            if profit > 0:
                max_profit += profit
        return max_profit


assert Two.maxProfit(case1) == 7
assert Two.maxProfit(case2) == 0
