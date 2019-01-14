# Problem Definition of Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears **more than** *⌊ n/2 ⌋* times.

You may assume that the array is non-empty and the majority element always exist in the array.

**Example 1**:

    Input: [3,2,3]
    Output: 3

## Method
    Counting problem: using get() method of dictionary
## Python Code

```python
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # New dictionary
        dic = {}
        for item in nums:
            # get() method
            dic[item] = dic.get(item, 0)+1
        return max(dic, key=dic.get)
```

## Java Code

```java

```