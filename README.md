# leetcode_answers_python
Codes and Answers of Leetcode Problems in Python

|\#|Method|Code|Difficulty|Recommend|
|:--|:-----|:-----:|:----------:|:----:|
|1|[Two Sum 两数之和](https://leetcode-cn.com/problems/two-sum/)|[python](/1_100/1.py)|Easy|
|3|[Longest Substring Without Repeating Characters 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)|[python](/1_100/3.py)|Medium|
|7|[Reverse Integer 整数反转](https://leetcode-cn.com/problems/reverse-integer/)|[python](/1_100/7.py)|Easy|
|8|[String to integer 字符串转换整数（atoi）](https://leetcode-cn.com/problems/string-to-integer-atoi/)|[python](/1_100/8.py)|Medium|
|14|[Longest common prefix 最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/)|[python](/1_100/14.py)|Easy|
|28|[Implement strstr 实现strStr()](https://leetcode-cn.com/problems/implement-strstr/)|[python](/1_100/28.py)|Easy|
|38|[Count and Say 报数](https://leetcode-cn.com/problems/count-and-say/)|[python](/1_100/38.py)|Easy|5|
|48|[Rotate image](/1_100/48.md)|[python](/1_100/48.py)|Medium|
|122|[Best Time to Buy and Sell Stock II 买卖股票的最佳时期2](/101_200/122_best_time_to_buy_and_sell_stock.md)|[python](/101_200/122.py)|Easy|
|344|[Reverse String 反转字符串]()|[python](/301_400/344.py)|Easy|


	Using helper decorator @time_it to see performance directly 

	使用装饰器 @time_it 来直观对比多种方法的时间性能

[**@time_it decorator**](/sechema.py)
```python
def time_it(func):
    @wraps(func)
    def inner(*args):
        date = ('{}-{}-{} {}:{}:{}').format(*time.localtime(time.time()))
        t0 = time.perf_counter_ns()
        _result = func(*args)
        elapsed = (time.perf_counter_ns() - t0)/1000
        if _result:
            print(f'[{date}]: [{elapsed:0.4f}ms]{func.__name__} -> {_result}')
        else:
            print(f'[{date}]: [{elapsed:0.4f}ms]{func.__name__}')
        return _result
    return inner
```

**Code example:**

```python3
# /301_400/344.py
# 反转字符串

import sys
sys.path.append('.')
from schema import time_it


class Solution:
    @time_it
    def tow_pointers(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left + 1 <= right - 1:
            if s[left] != s[right]:
                s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    @time_it
    def build_in_reserve(self, s: list) -> None:
        s.reverse()


solu = Solution()
s1 = ["h", "e", "l", "l", "o"]
s2 = ["H", "a", "n", "n", "a", "h"]

solu.tow_pointers(s1)
solu.tow_pointers(s2)
assert ''.join(s1) == 'olleh'
assert ''.join(s2) == 'hannaH'

solu.build_in_reserve(s1)
solu.build_in_reserve(s2)
assert ''.join(s1) == 'hello'
assert ''.join(s2) == 'Hannah'


"""
example output:

[2019-7-18 21:46:25]: [4.3910ms]tow_pointers
[2019-7-18 21:46:25]: [2.8640ms]tow_pointers
[2019-7-18 21:46:25]: [1.9380ms]build_in_reserve
[2019-7-18 21:46:25]: [0.5760ms]build_in_reserve
"""
```


---
Please Checkout [TODO](/TODO.md) to see what's the plan next

It is welcomed to open issues if you wanna help : )
