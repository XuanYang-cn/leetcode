# Problem Definition of Merge_Two_Sorted_lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

**Example 1**:

    Input: 1->2->4, 1->3->4

    Output: 1->1->2->3->4->4

## Method

    Two Pointers

## Python Code

```python
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        if l1.val <= l2.val:
            small = l1
            pointerl1 = l1
            pointerl2 = l2
        else:
            small = l2
            pointerl1 = l2
            pointerl2 = l1

        while pointerl1 is not None:
            if pointerl2 is None:
                return small
            if pointerl1.next is None:
                pointerl1.next = pointerl2
                return small
            # insert
            elif pointerl2.val >= pointerl1.val and pointerl2.val <= pointerl1.next.val:
                temp = pointerl2
                pointerl2 = pointerl2.next
                temp.next = pointerl1.next
                pointerl1.next = temp
                pointerl1 = pointerl1.next
            elif pointerl2.val > pointerl1.next.val:
                pointerl1 = pointerl1.next

```

## Java Code

```java

```