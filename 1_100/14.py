'''14. Longest common prefix 最长公共前缀'''

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'


import sys
sys.path.append('.')
from schema import time_it


class Solution:
    @time_it
    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) <= 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        common = strs[0]
        for i in range(1, len(strs)):
            common = self.find_common_prefix(common, strs[i])
            if common == "" or common is None:
                return common
        return common

    def find_common_prefix(self, s1, s2) -> str:
        length = min(len(s1), len(s2))
        i = 0
        while i < length:
            if s1[i] == s2[i]:
                i += 1
            else:
                return s1[:i]
        return s1[:i]

    @time_it
    def longestCommonPrefix1(self, strs: list) -> str:
        '''solve short string problem
            Time:
                worst:
                    O(n*m) if all strings have the same length
                    n is the length of the strs, m is the length of th strings
                best:
                    O(n * minlength)
            Space: O(1)
        '''
        if len(strs) <= 0 or not strs[0]:
            return ""
        elif len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0])):
            for item in strs:
                if i > len(item)-1 or strs[0][i] != item[i]:
                    return strs[0][:i]
        return strs[0]

solu = Solution()
strs = ["flower","flow","flight"]
strs1 = ['a', 'a']

solu.longestCommonPrefix(strs)
solu.longestCommonPrefix1(strs)

solu.longestCommonPrefix1(strs1)
