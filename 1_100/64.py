# 64 Minimum path sum 最小路径和

__author__ = "Yang Xuan (jumpthepig@gmail.com)"


class Solution:
    def recursively(self, grid):
        '''run out of time'''
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        return self.mov(grid, 0, 0, len(grid), len(grid[0]))

    def mov(self, grid, x, y, m, n):
        if x == m or y == n:
            return float("Inf")
        if x == m - 1 and y == n - 1:
            return grid[x][y]
        else:
            return grid[x][y] + min(
                self.mov(grid, x, y+1, m, n),
                self.mov(grid, x+1, y, m, n))

    def two_dimen_dp(self, grid):
        '''
        dp[i][j]: 从(i, j) 走到终点的最短路径
        '''
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = grid[-1][-1]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m - 1 and j != n - 1:
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
                elif i != m - 1 and j == n - 1:
                    dp[i][j] = grid[i][j] + dp[i + 1][j]
                elif i != m - 1 and j != n - 1:
                    dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j + 1])
                else:
                    dp[i][j] = grid[i][j]
        return dp[0][0]
        pass
