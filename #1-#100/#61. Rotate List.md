# Problem Definition of Rotate List

Given a linked list, rotate the list to the right by k places, where k is non-negative.

**Example 1**:

    Input: 1->2->3->4->5->NULL, k = 2
    utput: 4->5->1->2->3->NULL
    Explanation:
    rotate 1 steps to the right: 5->1->2->3->4->NULL
    rotate 2 steps to the right: 4->5->1->2->3->NULL

**Example 2**:

    Input: 0->1->2->NULL, k = 4
    Output: 2->0->1->NULL
    Explanation:
    rotate 1 steps to the right: 2->0->1->NULL
    rotate 2 steps to the right: 1->2->0->NULL
    rotate 3 steps to the right: 0->1->2->NULL
    rotate 4 steps to the right: 2->0->1->NULL

**Note**:

## Method

1. Calculating the length of List
2. Find the Tail, let $tail.next = head$ --> making List a circle-LinkedList
3. Shifting tail along with head
4. let $tail.next = None$, Over

## Python Code

```python
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head or not head.next:
            return head

        # Calculating Length of LinkedList, and find the TAIL  --> which is the last ListNode of a List
        length = 1
        pointer = head
        while pointer.next:
            length += 1
            pointer = pointer.next
        tail = pointer  # Tail of Linked List
        tail.next = head  # circle

        N = length - k % length  # Steps that head moves right

        for i in range(N):
            head = head.next
            tail = tail.next  # Tail moves along with head

        tail.next = None

        return head
```

## Java Code

```java

```