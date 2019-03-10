# Problem Definition of Two_Sum_II - Input array is sorted

    Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

    The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

**Note:**

* Your returned answers (both index1 and index2) are not zero-based.
* You may assume that each input would have exactly one solution and you may not use the same element twice.


**Example 1**:

    Input: numbers = [2,7,11,15], target = 9

    Output: [1,2]

    Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

## Method

    Two Pointers
    
    If sum is greater than target, right_pointer - 1
    
    If summation is less than target, left_Pointer + 1

## Python Code

```python
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if numbers is None or len(numbers)<2:
            return []
        
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left+1,right+1]
```

## Java Code

```java

```