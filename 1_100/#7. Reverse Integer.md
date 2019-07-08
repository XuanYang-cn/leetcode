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

## Python Code
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
## Java Code
```java
class Solution{
    public int reverse(int x) {
        // Use long to store x, because if x is -2147483648, then -x is 2147483648
        // which is larger than the max value of Integer
        long temp = x;
        int flag = 0;
        // if x is negative, change x to positive and let flag = -1
        if(temp < 0){
            flag = -1;
            temp = (-1) * temp;
        } else if(temp > 0){
            flag = 1;
        }
        // if x == 0, return x
        else{
            return 0;
        }
        // Note that result is always positive
        long result = 0;
        while(temp != 0){
            result = result * 10 + temp % 10;
            temp = temp / 10;
            // when x is positive, check if result is greater than 2^31-1(Overflow)
            // when x is negative, check if result is greater than 2^31, which means (-result) is less than -2^31(Overflow)
            // if Overflow, return 0
            if((flag == 1 && result > Integer.MAX_VALUE - 1) || (flag == -1 && result > Integer.MAX_VALUE)){
                return 0;
            }
        }
        // return the signed result
        return (int)result * flag;
    }
}
```