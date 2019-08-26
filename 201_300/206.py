# 206 reverse linkedlist 反转链表

__author__ = "Yang Xuan (jumpthepig@gmail.com)"


import sys
sys.path.append('.')
from schema import Linkedlist, time_it
from schema import Node as ListNode


class Solution:

    @classmethod
    @time_it
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            temp = head.next
            head.next = prev

            prev = head
            head = temp
        return prev


l1 = Linkedlist([5, 4, 3, 2, 1])
print(l1)
Solution.reverseList(l1.head)
