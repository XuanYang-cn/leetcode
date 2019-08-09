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

solu = Solution()
strs = ["flower","flow","flight"]

solu.longestCommonPrefix(strs)
