# 234 Palindrome linked list 回文链表

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'


import sys
sys.path.append('.')
from schema import time_it, Linkedlist
from schema import Node as ListNode


class Solution:
    @classmethod
    @time_it
    def isPalindrome(self, head: ListNode) -> bool:
        # Find middle
        first = head
        middle = head
        while first and first.next:
            first = first.next.next
            middle = middle.next
        if first:
            middle = middle.next

        # Reverse last half
        dump = ListNode(2524)

        prev = dump
        last = middle
        while last:
            temp = last.next
            last.next = prev

            prev = last
            last = temp

        while prev.next:
            if prev.val != head.val:
                return False
            else:
                prev = prev.next
                head = head.next
        return True


l1 = Linkedlist([1])
assert Solution.isPalindrome(l1.head)
l2 = Linkedlist([1, 2, 2, 1])
assert Solution.isPalindrome(l2.head)
l3 = Linkedlist([1, 2])
assert not Solution.isPalindrome(l3.head)


"""
example output:
[2019-8-28 16:27:43]: [2.1780ms]isPalindrome -> True
[2019-8-28 16:27:43]: [2.7910ms]isPalindrome -> True
[2019-8-28 16:27:43]: [1.4730ms]isPalindrome -> False
"""
