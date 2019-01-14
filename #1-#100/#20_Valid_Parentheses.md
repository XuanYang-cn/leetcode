# Problem Definition of Valid_Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

**Example 1**:

    Input: "()"

    Output: true

**Example 2**:

    Input: "()[]{}"

    Output: true

**Example 3**:

    Input: "([)]"

    Output: false

## Method

    Using a stack to store left parenthesis.

    For each parenthesis:

        if left_parenthesis, push left

        if right_parenthesis, pop and see if they are valid parentheses.

    Using a dictionary to store valid parentheses

## Python Code

```python
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parent = {")": "(", "]": "[", "}": "{"}
        for i in range(0, len(s)):
            if s[i] not in parent:
                stack.append(s[i])
            elif len(stack) == 0 or parent[s[i]] != stack.pop():
                return False
        return len(stack) == 0
```

## Java Code

```java

```