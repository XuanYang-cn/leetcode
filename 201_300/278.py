# 278 First bad version 第一个错误版本

__author__ = "Yang Xuan (jumpthepig@gamil.com)"


import sys
sys.path.append('.')
from schema import time_it

def isBadVersion(n):
    if n >= 4:
        return True
    else:
        return False


class Solution:
    @classmethod
    @time_it
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left < right:
            middle = (left + right) // 2

            if isBadVersion(middle):
                right = middle
            elif not isBadVersion(middle):
                left = middle + 1
        return right


case1 = 6
assert Solution.firstBadVersion(case1) == 4
