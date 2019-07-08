# Problem Definition of Binary Search

Given a **sorted** (in ascending order) integer array $nums$ of $n$ elements and a $target$ value, write a function to search $target$ in $nums$. If $target$ exists, then return its $index$, otherwise return $-1$.

**Example 1**:

    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

## Method

1. **Typical** Binary Search

## Python Code

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        return -1
```

## Java Code

```java

```