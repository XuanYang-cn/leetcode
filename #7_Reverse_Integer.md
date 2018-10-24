# Problem Definition of Reverse_Integer

Given a 32-bit signed integer, reverse digits of an integer.

**Example 1**:

    Input: -123

    Output: -321
**Example 3**:

    Input: 120

    Output: 21

**Note**:

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: $[-2^{−31},  2^{31} − 1]$. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

## Method

Basic Idea:

result = result*10 + x%10

## Code
```python
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #if x is negative, change x to positive and let flag = -1
        if x < 0:
            flag = -1
            x = -x
        elif x > 0:
            flag = 1
        else:
            return 0 #if x==0, return x
        result = 0 #Note that result is always positive
        Max = 2**31
        while x != 0:
            result = result*10 + x%10
            x = x//10 
            #when x is positive, check if result is greater than 2^31-1(Overflow)
            #when x is negative, check if result is greater than 2^31, which means (-result) is less than -2^31(Overflow)
            # if Overflow, return 0
            if (flag==1 and result > Max-1) or (flag ==-1 and result > Max):
                return 0
        #return the signed result
        return result*flag
```