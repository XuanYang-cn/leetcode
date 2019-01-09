# Problem Definition of Pascal's_Triangle_II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

![gif](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif "In Pascal's triangle, each number is the sum of the two numbers directly above it.")

**Example 1**:

    Input: 3
    Output: [1,3,3,1]

## Method

## Python Code

```python
class Solution:
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[] for i in range(rowIndex+1)]
        for i in range(0,rowIndex+1):
            if i == 0:
                result[0].append(1)
            else:
                for j in range(0, i+1):
                    if j == 0 or j == i:
                        result[i].append(1)
                    elif i > 1:
                        result[i].append(result[i-1][j-1] + result[i-1][j])
        return result[rowIndex]
```

## Java Code

```java

```