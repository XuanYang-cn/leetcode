# 242 valid anagram 有效的字母异位词

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'


import sys
sys.path.append('.')
from schema import time_it


class Solution:
    @classmethod
    @time_it
    def isAnagram(cls, s: str, t: str) -> bool:
        '''Sort and compare
        Time : O(Nlog(N))
        '''
        s = sorted(s)
        t = sorted(t)
        
        if s == t:
            return True
        else:
            return False

    @classmethod
    @time_it
    def hash_it(cls, s, t) -> bool:
        if len(s) != len(t):
            return False

        counter = {char: 0 for char in 'abcdefghijklmnopqrstuvwxyz'}

        for char in s:
            counter[char] += 1

        for char in t:
            counter[char] -= 1
            if counter[char] < 0:
                return False
        return True


case1 = ('anagram', 'nagaram')
case2 = ('rat', 'car')

assert Solution.isAnagram(*case1)
assert not Solution.isAnagram(*case2)
assert Solution.hash_it(*case1)
assert not Solution.hash_it(*case2)
