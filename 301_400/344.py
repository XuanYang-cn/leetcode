# /301_400/344.py
# 反转字符串

import sys
sys.path.append('.')
from schema import time_it


class Solution:
    @time_it
    def tow_pointers(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left + 1 <= right - 1:
            if s[left] != s[right]:
                s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    @time_it
    def build_in_reserve(self, s: list) -> None:
        s.reverse()


solu = Solution()
s1 = ["h", "e", "l", "l", "o"]
s2 = ["H", "a", "n", "n", "a", "h"]

solu.tow_pointers(s1)
solu.tow_pointers(s2)
assert ''.join(s1) == 'olleh'
assert ''.join(s2) == 'hannaH'

solu.build_in_reserve(s1)
solu.build_in_reserve(s2)
assert ''.join(s1) == 'hello'
assert ''.join(s2) == 'Hannah'

"""
example output:

[2019-7-18 21:46:25]: [4.3910ms]tow_pointers
[2019-7-18 21:46:25]: [2.8640ms]tow_pointers
[2019-7-18 21:46:25]: [1.9380ms]build_in_reserve
[2019-7-18 21:46:25]: [0.5760ms]build_in_reserve
"""
