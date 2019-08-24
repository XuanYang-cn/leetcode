# Problem Definition of Reverse Linked List

Reverse a singly linked list.

**Example 1**:

    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL

## Method

    Two pointers, one points to current node, the other points to previous node

$O(N)$ time complexity

$O(1)$ space complexity

## Python Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous = None
        current = head

        while current:
            head = head.next
            current.next = previous

            previous = current
            current = head

        return previous
```

## Java Code

```java

```