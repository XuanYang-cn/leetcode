# 477 Total hamming distance 汉明距离总和

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'

import sys
sys.path.append('')
from schema import time_it


class Solution(object):
    def hammingDistance(self, x, y):
        a = x ^ y
        count = 0

        while a != 0:
            count += 1
            a &= a-1
        return count

    @time_it
    def totalHammingDistance(self, nums):
        '''
        Brutal force
        Time: O(N), N is length of the nums
        Space: 1
        '''
        total = 0
        for i in range(len(nums) - 1):
            for j in range(i, len(nums)):
                total += self.hammingDistance(nums[i], nums[j])
        return total

    @time_it
    def compare_vertical(self, nums):
        '''
        Compare vertical
        Time: O(32 * N) = O(N), N is length of nums
        Space O(N)
        '''
        counts = [0 for _ in range(32)]
        result = 0
        mark = 1
        for i in range(32):
            for item in nums:
                if item & mark:
                    counts[i] += 1
            result += counts[i] * (len(nums) - counts[i])
            mark <<= 1  # 第i位设为1
        return result


case1 = [4, 14, 2]
solu = Solution()
assert solu.totalHammingDistance(case1) == 6
assert solu.compare_vertical(case1) == 6
