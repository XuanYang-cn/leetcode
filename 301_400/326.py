# 326 Power of Three 3 的 幂

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'


import math
import sys
sys.path.append('.')
from schema import time_it


class Solution:
    @classmethod
    @time_it
    def isPowerOfThree(self, n: int) -> bool:
        '''
        n = 3 ^ x
        Time: O(log(N))
        Space: 1
        '''
        if n < 1:
            return False
        while n % 3 == 0:
            n = n // 3
        return n == 1

    @classmethod
    @time_it
    def brutal_buildins(self, n):
        return n > 0 and 3 ** round(math.log(n, 3)) == n

    @classmethod
    @time_it
    def math_buildins(self, n):
        '''
        Time: UNKNOWN
        '''
        return (math.log10(n) / math.log10(3)) % 1 == 0


case0 = 3
assert Solution.isPowerOfThree(case0)
assert Solution.brutal_buildins(case0)
assert Solution.math_buildins(case0)
case1 = 59049
assert Solution.isPowerOfThree(case1)
assert Solution.brutal_buildins(case1)
assert Solution.math_buildins(case1)
case2 = 3 ** 19
assert Solution.isPowerOfThree(case2)
assert Solution.brutal_buildins(case2)
assert Solution.math_buildins(case2)
