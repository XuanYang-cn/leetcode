# 3. longest substring without repeating characters 无重复字符的最长子串

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'


import sys
sys.path.append('.')
from schema import time_it


class Solution:
    @classmethod
    @time_it
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left = 0
        right = 1
        length = 1
        while right < len(s):
            if s[right] in s[left:right]:
                index = s.find(s[right], left, right)
                right += 1
                left = index + 1
            else:
                right += 1
                length = max(length, right-left)
        return length


case1 = 'abcabcbb'
assert Solution.lengthOfLongestSubstring(case1) == 3

case2 = 'pwwkew'
assert Solution.lengthOfLongestSubstring(case2) == 3


"""
example output:
[2019-8-25 0:7:35]: [13.7410ms]lengthOfLongestSubstring -> 3
[2019-8-25 0:7:35]: [11.8850ms]lengthOfLongestSubstring -> 3
"""
