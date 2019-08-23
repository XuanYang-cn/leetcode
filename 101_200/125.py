# 125 is palindrome

__author__ = "Yang Xuan (jumpthepig@gmail.com)"


import sys
sys.path.append('.')
from schema import time_it


class Solution:
    @classmethod
    @time_it
    def isPalindrome(self, s):
        """
        Time: O(N) + O(N) + O(N/2) = O(N)
        Space: O(N)
        Too slow
        """
        lists = []
        # Transforming string s to list lists
        # and remove all characters those aren't letters or numbers
        # and change letters to lowercase
        for i in range(0, len(s)):
            if s[i].isalnum():
                lists.append(s[i].lower())
        # list is mutable, thus we have to use copy()
        # method to copy a lists rather than "="
        temp = lists.copy()

        # reverse a list
        lists.reverse()
        if temp == lists:
            return True
        else:
            return False

    @classmethod
    @time_it
    def two_pointers(self, s):
        """
        Time: O(N)
        Space: O(1)
        """
        # left pointer points the left side of stirng s
        # right pointer points the right side of string s
        left = 0
        right = len(s)-1
        while(left < right):
            # find the letter or number we need for comparing, ignore others
            while left < right and not s[left].isalnum():
                left = left+1
            # same as above
            while left < right and not s[right].isalnum():
                right = right-1
            # compare the lowercase of founded char
            if s[left].lower() != s[right].lower():
                return False
            # Iterator until left pointer is not less than right pointer
            left = left+1
            right = right-1
        return True


case1 = "A man, a plan, a canal: Panama"
case2 = "race a car"

assert Solution.isPalindrome(case1)
assert Solution.two_pointers(case1)

assert not Solution.isPalindrome(case2)
assert not Solution.two_pointers(case2)
