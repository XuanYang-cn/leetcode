# 21 Merge two sorted list 合并两个有序链表

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'


import sys
sys.path.append('.')
from schema import Linkedlist, time_it
from schema import Node as ListNode


class Solution:
    @classmethod
    @time_it
    def tow_pointers(self, l1, l2):
        dump = ListNode(2524)
        pointer = dump

        while l1 and l2:
            if l1.val <= l2.val:
                pointer.next = l1
                l1 = l1.next
                pointer = pointer.next
            else:
                pointer.next = l2
                l2 = l2.next
                pointer = pointer.next

        if l1:
            pointer.next = l1
        if l2:
            pointer.next = l2
        return dump.next


l1 = Linkedlist([1, 2, 4])
l2 = Linkedlist([1, 3, 4])
Solution.tow_pointers(l1.head, l2.head)
