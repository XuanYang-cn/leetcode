# Problem Description of Palindrome_Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

**Example** 1:

Input: 121

Output: true

## Method

key method: Revert Half Of the Number

## Code

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