# 7 reverse integer 整数反转

__author__ = "Yang Xuan (jumpthepig@gmail.com)"

import sys
sys.path.append('.')
from schema import time_it


class Solution:
    @time_it
    def reverse(self, x):
        '''
        result = result*10 + x%10
        '''
        # if x is negative, change x to positive and let flag = -1
        flag = 1
        if x == 0:
            return 0
        elif x < 0:
            flag = -1
            x = -x

        result = 0  # Note that result is always positive
        MAX = 2 ** 31

        while x > 0:
            result = result * 10 + x % 10
            x //= 10

            # when x is positive, check if result > 2^31-1 (Overflow)
            # when x is negative, check if result > 2^31(-result < -2^31)
            # if Overflow, return 0
            if (flag == 1 and result > MAX-1) or\
               (flag == -1 and result > MAX):
                return 0

        # return the signed result
        return result * flag


case1 = 123
case2 = -123
solu = Solution()
r1 = solu.reverse(case1)
assert r1 == 321
r2 = solu.reverse(case2)
assert r2 == -321


"""
example output:
[2019-8-25 0:13:37]: [3.4080ms]reverse -> 321
[2019-8-25 0:13:37]: [2.6430ms]reverse -> -321
"""
