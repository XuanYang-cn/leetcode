# Problem Definition of Valid_Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

**Note** For the purpose of this problem, we define empty string as valid palindrome.

**Example 1**:

    Input: "A man, a plan, a canal: Panama"

    Output: true

## Method 1

Basic Idea:

Using list and its method of Python

## Python Code 1
```python
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lists = []
        # Transforming string s to list lists, and remove all characters those aren't letters or numbers, and change letters to lowercase
        for i in range(0,len(s)):
            if s[i].isalnum():
                lists.append(s[i].lower())
        #list is mutable, thus we have to use copy() method to copy a lists rather than "="
        temp = lists.copy()
        # reverse a list
        lists.reverse()
        if temp == lists:
            return True
        else:
            return False
```

## Method 2

Basic Idea:

2 - pointer

## Python Code 2
```python
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #left pointer points the left side of stirng s
        #right pointer points the right side of string s
        left = 0
        right = len(s)-1
        while(left < right):
            #find the letter or number we need for comparing, ignore others
            while left < right and not s[left].isalnum():
                left = left+1
            # same as above
            while left < right and not s[right].isalnum():
                right = right-1
            # compare the lowercase of founded char
            if s[left].lower() != s[right].lower():
                return False
            #Iterator until left pointer is not less than right pointer
            left = left+1
            right = right-1
        return True
```
## Java Code

```