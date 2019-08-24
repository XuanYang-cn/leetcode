# 1 two sum 两数之和

__author__ = "Yang Xuan (jumpthepig@gmail.com)"

import sys
sys.path.append('.')
from schema import time_it


@time_it
def twoSum(nums, target):
    """
    Space: O(N)
    Average Time: O(N/2)
    """
    # Change list into dictionary.
    # dictionary_keys are values of list nums
    # dictionary_value are indexes of list nums
    ref = {value: index for (index, value) in enumerate(nums)}

    for index, value in enumerate(nums):
        searchback = ref.get(target - value, None)
        if searchback != index:
            return [index, searchback]
        else:
            continue


nums = [2, 7, 11, 15]
target = 9
a = twoSum(nums, target)
assert a == [0, 1]


"""
example output:
[2019-8-24 23:55:38]: [3.9910ms]twoSum -> [0, 1]
"""
