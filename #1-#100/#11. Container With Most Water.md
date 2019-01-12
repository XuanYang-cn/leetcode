# Problem Definition of Container With Most Water

Given n non-negative integers $a_1, a_2, ..., a_n$ , where each represents a point at coordinate $(i, a_i)$. $n$ vertical lines are drawn such that the two endpoints of line i is at $(i, a_i)$ and $(i, 0)$. Find two lines, which together with x-axis forms a container, such that the container contains the most water.

**Note:** You may not slant the container and *n* is at least 2.

![graph](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg "The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.")

**Example 1**:

    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49

**Note**:

## Method

    Two Pointers

## Python Code

```python
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Two Pointers
        left = 0
        right = len(height) - 1
        area = float("-Inf")

        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return area
```

## Java Code

```java

```