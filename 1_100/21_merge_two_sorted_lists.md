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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(2524)  # Building a Header makes code more readable
        pointer = head

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

        return head.next

```

## Java Code

```java

```