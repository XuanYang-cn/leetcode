# Problem Definition of Two_Sum

    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Example 1**:

    Input: nums = [2, 7, 11, 15], target = 9

    Because nums[0] + nums[1] = 2 + 7 = 9,
    Output: [0, 1]

## Method

    Change List into Dictionary

## Python Code

```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Change list into dictionary.
        # dictionary_keys are values of list nums
        # dictionary_value are indexes of list nums
        ahash = {}
        for i in range(len(nums)):
            ahash[nums[i]] = i
        for j in range(len(nums)):
            forsearch = target - nums[j]
            if forsearch in ahash and ahash[forsearch] != j:
                return [j,ahash[forsearch]]
            else:
                continue
```

## Java Code

```java

```