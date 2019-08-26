# 19 Remove Nth node from end of the linkedlist 删除链表的倒数第N个结点

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'


import sys
sys.path.append('.')
from schema import Linkedlist, time_it
from schema import Node as ListNode


class Solution:
    @classmethod
    @time_it
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        tow pointers
        '''
        dum = ListNode(2524)
        dum.next = head
        first = dum
        second = dum

        sep = 0
        while sep <= n:
            first = first.next
            sep += 1

        while first:
            second = second.next
            first = first.next

        second.next = second.next.next

        return dum.next


l1 = Linkedlist([4, 3, 2, 1, 0])
Solution.removeNthFromEnd(l1.head, 2)


"""
example output:
[2019-8-26 19:50:51]: [2.8700ms]removeNthFromEnd -> 4 -> 3 -> 2 -> 0 -> None
"""
