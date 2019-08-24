# 8 String to integer 字符串转换整数（atoi）

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'

import sys
sys.path.append('.')
from schema import time_it


class Solution:
    @classmethod
    @time_it
    def myAtoi(self, s: str) -> int:
        if len(s) == 0 or not s:
            return 0

        flag = 1
        result = 0
        INT_MIN = - (2 ** 31)
        INT_MAX = 2 ** 31 - 1

        for i in range(len(s)):
            if s[i] == ' ':
                continue
            elif not s[i].isdigit():
                if s[i] == '+':
                    if i == len(s)-1 or not s[i+1].isdigit():
                        return 0
                    i += 1
                    break
                elif s[i] == '-':
                    if i == len(s)-1 or not s[i+1].isdigit():
                        return 0
                    i += 1
                    flag = -1
                    break
                else:
                    return 0
            else:
                break

        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            if flag > 0 and result > INT_MAX:
                return INT_MAX
            elif flag < 0 and -result < INT_MIN:
                return INT_MIN

            i += 1

        return result*flag


case1 = "   -42"
r1 = Solution.myAtoi(case1)
assert r1 == -42
case2 = "4193 with words"
r2 = Solution.myAtoi(case2)
assert r2 == 4193
case3 = "words and 987"
r3 = Solution.myAtoi(case3)
assert r3 == 0
case4 = "-91283472332"
r4 = Solution.myAtoi(case4)
assert r4 == -2147483648
