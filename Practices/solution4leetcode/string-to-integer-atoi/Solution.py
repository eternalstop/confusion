#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @return an integer
    def atoi(self, str):
        if not str:
            return 0
        s = str.strip()
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        sign = True
        if s[0] == '-':
            sign = False
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        ans = 0
        for char in s:
            if char.isdigit():
                ans = ans * 10 + int(char)
            else:
                break
        if sign == False:
            ans = -ans
        if ans > INT_MAX:
            return INT_MAX
        elif ans < INT_MIN:
            return INT_MIN
        else:
            return ans


s = Solution()
print s.atoi("1")

