# Problem Definition of Remove_Duplicates_from_Sorted_List

Given a sorted linked list, delete all duplicates such that each element appear only once.

**Example 1**:

    Input: 1->1->2

    Output: 1->2
**Example 2**:

    Input: 1->1->2->3->3

    Output: 1->2->3

## Method

Basic Idea:

Since the given linked list is sorted. If $current.next.val$ **is equal to** $current.val$, remove $current.next$.

## Python Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #return [] if single-linked list head is null
        if head == None:
            return []
        #current node
        current = head
        #while current.next node exists
        while current.next:
            if current.next.val == current.val:
                current.next = current.next.next#remove current.next node if current.next.val equals to current.val
            else:
                #else keep on iterating
                current = current.next
        return head
```