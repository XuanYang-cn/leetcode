# 5 Longest Palindromic substring 最长回文子串

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'


class Solution:
    def palindromic(self, s):
        n = len(s)
        if n <= 1:
            return s
        dp = [[False for _ in range(n)] for _ in range(n)]
        max_length = 1
        result = s[0]

        for j in range(n):
            for i in range(j):
                dp[i][j] = s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1])
                if dp[i][j] and max_length < j - i + 1:
                    max_length = j - i + 1
                    result = s[i: j + 1]
        return result
