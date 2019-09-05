# 191 Number of 1 bits 位1的个数

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'

import sys
sys.path.append('.')
from schema import time_it


class Solution(object):
    @classmethod
    @time_it
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            n &= n-1
            count += 1
        return count


case1 = 11  # 00000000000000000000000000001011
assert Solution.hammingWeight(case1) == 3
