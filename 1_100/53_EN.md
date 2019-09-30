# Problem Definition of Maximum_Subarray

Given an integer array **nums**, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

最大子数组问题

**Example 1**:

    Input:[-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

## Method

### Method 1: Brutal

There are
$C^1_{n} + C^2_{n-1} + ... + C^n_n$
subarrays for *nums[n]*.
Calculate all subarrays' sums and return the max

Time complexity: $O(N^2)$

No code ;)

### Method 2: Divide and Conquer
Refer to *Introduction to Algorithms* page 39-41

    There are three possible ways where the max_subarray is:

    1. Between [low, mid]
    2. Between [mid+1, high]
    3. Crossing mid(find the max_left in [i,mid] and max_right in [mid+1,j])
    note: Crossing means mid and mid+1 must be included

Time Complexity: $O(n\lg{n})$

**Note:** Easy to understand

### Python Code of Method 2: Divide and Conquer

```python
class Solution:
    # Using recursion
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Prepare for recursion in definition maxSub
        low = 0
        high = len(nums) - 1
        a = self.maxSub(nums, low, high)
        return a

    def maxSub(self, nums, low, high):
        """
        :type nums: List[int]
        :type low: int
        :type high: int
        :rtype: int
        """
        # If there is one element in nums, return this element.
        if low == high:
            return nums[low]
        else:
            mid = int((low + high) / 2)
            # Max value of left sub-array
            maxleftSub = self.maxSub(nums, low, mid)

            # Max value of right sub-array
            maxrightSub = self.maxSub(nums, mid + 1, high)

            # Max value of crossing sub-array
            maxCrossSub = self.maxCrossingSubArray(nums, low, high)

            # Return the max of those three above
            return max(maxleftSub, maxrightSub, maxCrossSub)

    def maxCrossingSubArray(self, nums, low, high):
        """
        Given an array nums and it's index, calculate the crossing sub-array
        :type nums: List[int]
        :type low: int
        :type high: int
        :rtype: int
        """
        # Calculate max_left in [i,mid]
        mid = int((low + high) / 2)
        left_sum = float('-Inf')# Make sure sums[mid] is included
        sum = 0
        for i in range(mid, low - 1, -1):
            sum = sum + nums[i]
            if sum > left_sum:
                left_sum = sum
                # max_left = i , i is the index

        # Calculate max_right in [mid+1,j]
        sum = 0
        right_sum = float("-Inf")# Make sure sums[mid+1] is included
        for j in range(mid + 1, high + 1):
            sum = sum + nums[j]
            if sum > right_sum:
                right_sum = sum
                # max_right = j, j is the index

        return left_sum + right_sum
```

### Method 3: Dynamic Programming

Status: $DP[i]$ means the max sum with $nums[i]$ ended

State transition equation: $DP[i] =  max(DP[i-1] + nums[i], nums[i])$

$max\_sum = max(DP[i], max\_sum)$

Time Complexity: $O(N)$

**Note:** hard to comprehend

### Python Code of Method 3: Dynamic Programming

```python
def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Using Dynamic Programming
    maxSubArrayEndsWithI = nums[0]
    max_sum = maxSubArrayEndsWithI
    for i in range(1, len(nums)):
        maxSubArrayEndsWithI = max(maxSubArrayEndsWithI + nums[i], nums[i])
        max_sum = max(maxSubArrayEndsWithI, max_sum)
    return max_sum
```
