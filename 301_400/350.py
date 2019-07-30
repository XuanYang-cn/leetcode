# 350. intersection of two arrays II
__author__ = 'Xuan Yang (jumpthepig2@gmail.com)'

import sys
sys.path.append('.')

from schema import time_it
class Solution:
    @time_it
    def intersect(self, nums1: list, nums2: list) -> list:
        '''Maker smaller one a dictionary
        space: O(n)
        time: O(n)
        '''
        if not nums1 or not nums2 or len(nums1) <= 0 or len(nums2) <= 0:
            return []

        (shorter, longer) = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)

        hash_shorter = {}
        for item in shorter:
            hash_shorter[item] = hash_shorter.get(item, 0) + 1

        result = []
        for item in longer:
            if item in hash_shorter:
                if hash_shorter[item] > 0:
                    result.append(item)
                    hash_shorter[item] -= 1

        return result

    @time_it
    def intersect1(self, nums1, nums2):
        '''
        ADVANCE 1: If nums1 and nums2 are sorted
        Solution: Two pointers
        '''
        pointer1 = 0
        pointer2 = 0
        result = []
        while pointer1 < len(nums1) and pointer2 < len(nums2):
            if nums1[pointer1] == nums2[pointer2]:
                result.append(nums1[pointer1])
                pointer1 += 1
                pointer2 += 1
            elif nums1[pointer1] > nums2[pointer2]:
                while pointer2 < len(nums2) - 1:
                    if nums2[pointer2 + 1] == nums2[pointer2]:
                        pointer2 += 1
                    else:
                        pointer2 += 1
                        break
            else:
                while pointer1 < len(nums1) - 1:
                    if nums1[pointer1 + 1] == nums1[pointer1]:
                        pointer1 += 1
                    else:
                        pointer1 += 1
                        break
        return result



nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

solu = Solution()

solu.intersect(nums1, nums2)

nums1 = [1, 1, 2, 2]
nums2 = [2, 2]
solu.intersect1(nums1, nums2)

nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
nums2 = [4, 7]
solu.intersect(nums1, nums2)
solu.intersect1(nums1, nums2)
