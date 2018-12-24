# Problem Definition of

    Given two sorted integer arrays *nums1* and *nums2*, merge *nums2* into *nums1* as one sorted array.

**Note:**

The number of elements initialized in *nums1* and *nums2* are *m* and *n* respectively.
You may assume that *nums1* has enough space (size that is greater or equal to m + n) to hold additional elements from *nums2*.

**Example 1**:

    Input:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3

    Output:[1,2,2,3,5,6]

## Method

## Python Code

```python
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n > 0:
            for i in range(0, n):
                nums1[i] = nums2[i]
            return
        elif n == 0:
            return
        current = n+m-1
        pointer1 = m-1
        pointer2 = n-1
        while current >= 0:
            if pointer1 < 0 or (nums2[pointer2] >= nums1[pointer1]):
                if pointer2 < 0:
                    return
                nums1[current] = nums2[pointer2]
                pointer2 -= 1
                current -= 1
            elif pointer2 < 0 or nums2[pointer2] < nums1[pointer1]:
                nums1[current] = nums1[pointer1]
                pointer1 -= 1
                current -= 1
        return
```

## Java Code

```java

```