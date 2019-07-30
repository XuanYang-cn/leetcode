"""
189.Rotate array
旋转数组
"""
import sys
sys.path.append('.')
from schema import time_it


class Solution:
    @time_it
    def rotate(self, nums: list, k: int) -> None:
        k %= len(nums)
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


nums1 = [1, 2, 3, 4, 5, 6, 7]
param1 = (nums1, 3)

nums2 = [-1, -100, 3, 99]
param2 = (nums2, 2)

nums3 = [1, 2]
param3 = (nums3, 3)

solu = Solution()

solu.rotate(*param1)
assert nums1 == [5, 6, 7, 1, 2, 3, 4]

solu.rotate(*param2)
assert nums2 == [3, 99, -1, -100]

solu.rotate(*param3)
assert nums3 == [2, 1]
