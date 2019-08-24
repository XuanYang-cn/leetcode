# Problem Definition of Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer $pos$ which represents the position $(0-indexed)$ in the linked list where tail connects to. If $pos$ is $-1$, then there is no cycle in the linked list.

**Example 1**:

    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where tail connects to the second node.

![](../others/graphs/141circularlinkedlist.png )

**Note**:

## Method

Two Pointers with different speed

## Python Code

```python
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        faster = head.next
        slower = head

        while faster and faster.next:
            if faster is slower:  # If cycle, faster and slower will eventually meet
                return True
            faster = faster.next.next  # Moves 2 step a time
            slower = slower.next  # Moves 1 step a time

        return False
```

## Java Code

```java

```