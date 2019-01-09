# Problem Definition of Best_Time_to_Buy_and_Sell_Stock

Say you have an array for which the $i^{th}$ element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

**Example 1**:

    Input: [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

**Example 2**:

    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.

## Method

## Python Code

```python
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Clever
        if not prices:
            return 0
        min_left = float('Inf')
        max_prof = 0

        for i in range(len(prices)):
            if prices[i] < min_left:
                min_left = prices[i]
            elif prices[i] - min_left > max_prof:
                max_prof = prices[i] - min_left
        return max_prof
```

## Java Code

```java

```