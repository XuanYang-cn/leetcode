# Problem Description of Palindrome_Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

**Example** 1:

Input: 121

Output: true

## Method

key method: Revert Half Of the Number

## Python Code

```python
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 10 and x >=0:#if x is less than 10 and greater than eqauls to 0, x is a palindrome number
            return True
        elif x < 0 or x%10 == 0:#if x is less than 0, or divisible by 10, x is not a palindrome number
            return False
        back = 0
        while x > back:
            back = back*10+x%10
            x=x//10
        if back == x or back//10 == x:
            return True
        else:
            return False
```

## Java Code

```java
class Solution {
    // The Java code provide another solution
    // Firstly if the x is lower than 0, then x is not a palindrome
    // Secondly reverse the number x, judge if the reverse of x equals x
    public boolean isPalindrome(int x) {
        long temp = x;
        // if x is negative, then x is not a palindrome
        if(temp < 0)
            return false;

        // Note that result is always positive
        long result = 0;
        while(temp != 0){
            result = result * 10 + temp % 10;
            temp = temp / 10;
            // when x is positive, check if result is greater than 2^31-1(Overflow)
            // when x is negative, check if result is greater than 2^31, which means (-result) is less than -2^31(Overflow)
            // if Overflow, return false, because if x is a Integer and its reverse is not a Integer
            // then x does not equals to the reverse of x, then x is not a palindrome
            if(result > Integer.MAX_VALUE - 1){
                return false;
            }
        }
        // return the signed result
        return (int)result == x ? true : false;
    }
}
```