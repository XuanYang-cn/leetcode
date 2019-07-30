import sys
sys.path.append('.')
from schema import time_it

class Solution:
    @time_it
    def containsDuplicate(self, nums: list) -> bool:
        set_nums = set(nums)
        if len(set_nums) < len(nums):
            return True
        else:
            return False

    @time_it
    def containsDuplicate2(self, nums: list) -> bool:
        hash_nums = {}
        for item in nums:
            if item in hash_nums:
                return True
            else:
                hash_nums[item] = 1

        return False


nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

solu = Solution()

assert solu.containsDuplicate(nums1)
assert not solu.containsDuplicate(nums2)
assert solu.containsDuplicate(nums3)

assert solu.containsDuplicate2(nums1)
assert not solu.containsDuplicate2(nums2)
assert solu.containsDuplicate2(nums3)

