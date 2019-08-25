# 28 implement strstr 实现strStr()

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'

import sys
sys.path.append('.')
from schema import time_it


class Solution:
    @classmethod
    @time_it
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or len(needle) == 0:
            return 0

        if len(haystack) < len(needle):
            return -1

        #  breakpoint()

        begin = 0
        while True:
            while begin < len(haystack) and haystack[begin] != needle[0]:
                begin += 1

            if begin == len(haystack):
                return -1
            elif haystack[begin: begin+len(needle)] == needle:
                return begin
            else:
                begin += 1


case2 = ('aaaa', 'bba')
Solution.strStr(*case2)
case1 = ('hello', 'll')
Solution.strStr(*case1)


"""
example output:
[2019-8-25 22:29:26]: [4.4820ms]strStr -> -1
[2019-8-25 22:29:26]: [4.4960ms]strStr -> 2
"""
