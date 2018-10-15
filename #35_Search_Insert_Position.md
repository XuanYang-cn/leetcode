<!-- TOC -->

- [Problem Description of Search_Insert_Position](#problem-description-of-search_insert_position)
    - [Method](#method)
    - [Code](#code)
    - [Further Reading](#further-reading)
        - [Other kinds of Binary Search](#other-kinds-of-binary-search)
        - [二分查找的变种](#二分查找的变种)

<!-- /TOC -->
# Problem Description of Search_Insert_Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume **no duplicates** in the array. 

给定一个排好序的数组和目标值，如果数组中查询到了目标值，则返回该值的数组下标；若数组中查询不到目标值，返回按序插入该值的数组下标。

假设数组中**没有重复**的数。

## Method

Key Method: Binary search

Analysis : Find the **first** number that's **equal to or greater than** the **target** and return the index of the number.

Time Complexity: $O(logN)$

核心方法：二分查找（折半查找）

问题解析：在数组中找到第一个**大于等于**给定值的数，并返回该数的下标


## Code

```python
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            
            mid = (left + right)//2   #calculate middle point
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
    return left
```

## Further Reading

### Other kinds of Binary Search

- There are **duplicates** in array

1. Find the first equal to target
2. Find the fist greater than or equal to target
3. Find the fist greater than target
4. Find the last equal to target
5. Find the last lesser than or equal to target
6. Find the last lesser than target

### 二分查找的变种

- 有**重复**数据

找第一个与key相等的值，找第一个大于等于key的值，找第一个大于key的值

找最后一个与key相等的值，找最后一个小于等于key的值，找最后一个小于key的值
