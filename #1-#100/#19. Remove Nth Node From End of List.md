# Problem Definition of Remove Nth Node From End of List

**Example**:

    Given linked list: 1->2->3->4->5, and n = 2.

    After removing the second node from the end, the linked list becomes 1->2->3->5.

## Method

![](../others/graphs/19_Remove_nth_node_from_end_of_listB.png "Method")

## Python Code

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        Dum = ListNode(2524)
        Dum.next = head
        first = Dum
        second = Dum

        sep = 0
        while sep <= n:
            first = first.next
            sep += 1

        while first:
            second = second.next
            first = first.next

        second.next = second.next.next

        return Dum.next
```

## Java Code

```java

```