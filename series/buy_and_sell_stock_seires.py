"""
Best Time To Buy And Sell Stock Series
"""

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'


class Solution:
    """
    121. Best Time To Buy And Sell Stock 买卖股票的最佳时机
    Difficulty: Easy
    Description: 只允许完成一笔交易，即买入和卖出一支股票
    """

    @classmethod
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

    @classmethod
    def dynamic_programming(self, prices):
        if len(prices) == 0:
            return 0
        n = len(prices)

        dp_i_0 = 0  # 未开始时不持有股票的收益
        dp_i_1 = float("-Inf")  # 未开始时持有股票的收益
        for i in range(0, n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0  # 第n-1天不持有股票的最大收益


case1 = [7, 1, 5, 3, 6, 4]
case2 = [7, 6, 5, 4, 3, 2, 1]
assert Solution.brute_force(case1) == 5
assert Solution.brute_force(case2) == 0
assert Solution.one_traversal(case1) == 5
assert Solution.one_traversal(case2) == 0
assert Solution.dynamic_programming(case1) == 5
assert Solution.dynamic_programming(case2) == 0


class Two:
    """
    122. Best Time To Buy And Sell A Stock II 买卖股票的最佳时机2
    Difficulty: Easy
    Description: 能参与多次交易，但是必须在购买前出售掉之前的股票
    """

    @classmethod
    def maxProfit(self, prices) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            profit = prices[i+1] - prices[i]
            if profit > 0:
                max_profit += profit
        return max_profit

    @classmethod
    def Dynamic_programming(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        dp_i_0 = 0
        dp_i_1 = float("-inf")
        for i in range(0, n):
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0-prices[i])
        return dp_i_0


assert Two.maxProfit(case1) == 7
assert Two.maxProfit(case2) == 0
assert Two.Dynamic_programming(case1) == 7
assert Two.Dynamic_programming(case2) == 0


class Three:
    """
    123. Best Time To Buy And Sell A Stock III 买卖股票的最佳时机3
    Difficulty: Hard
    Description: 最多能完成2笔交易，但是必须在购买前出售掉之前的股票
    """
    def Dynamic_programming(self, prices):
        n = len(prices)
        max_k = 2
        if n == 0:
            return 0
        dp = [[[0 for _ in range(2)] for _ in range(max_k+1)] for _ in range(n)]

        for i in range(n):
            for k in range(max_k, 0, -1):
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue

                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
        return dp[n-1][max_k][0]


class Four:
    '''
    188. k
    '''
    def Dynamic_programming(self, prices, k):
        max_k = k
        n = len(prices)
        if n == 0:
            return 0
        if max_k > n//2:
            return self.max_profit_infi_k(prices)

        dp = [[[0 for _ in range(2)] for _ in range(max_k + 1)] for _ in range(n)]
        for i in range(n):
            for k in range(max_k, 0, -1):
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
        return dp[n-1][max_k][0]

    def max_profit_infi_k(self, prices):
        n = len(prices)
        for i in range(n):
            if i == 0:
                dp_i_0 = 0
                dp_i_1 = -prices[i]
                continue
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0-prices[i])
        return dp_i_0
