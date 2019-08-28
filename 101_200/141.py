# 141 Linked list cycle 环形链表

__author__ = "Yang Xuan (jumpthepig@gmail.com)"


import sys
sys.path.append('.')
from schema import time_it, Linkedlist
from schema import Node as ListNode


class Solution(object):
    @classmethod
    @time_it
    def two_pointers(self, head: ListNode):
        '''
        One pointer goes one step at a time
        The other pointer goes two steps at a time
        If is cycle: two pointer sooner or later will pointer to the same node
        If no cycle: the faster pointer will hit the end of the linked list
        '''
        dump = ListNode(2524)
        dump.next = head
        slower = dump
        faster = head

        while faster and faster.next:
            if slower is faster:
                return True
            slower = slower.next
            faster = faster.next.next

        return False


l1 = Linkedlist([3, 2, 0, -1])
n1 = l1.get_node(3)
n2 = l1.get_node(1)
n1.next = n2

assert Solution.two_pointers(l1.head)

l2 = Linkedlist([1, 2])
n1 = l2.get_node(1)
n2 = l2.get_node(0)
n1.next = n2
assert Solution.two_pointers(l2.head)

l3 = Linkedlist([1])
assert not Solution.two_pointers(l3.head)

"""
example output:
[2019-8-28 21:55:59]: [2.0180ms]two_pointers -> True
[2019-8-28 21:55:59]: [2.0800ms]two_pointers -> True
[2019-8-28 21:55:59]: [1.4350ms]two_pointers -> False
"""
