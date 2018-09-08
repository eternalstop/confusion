#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        try:
            float(s.strip())
        except ValueError:
            return False
        else:
            return True

s = Solution()
print s.isNumber("0")
print s.isNumber(" 0.1 ")
print s.isNumber("abc")
print s.isNumber("1 a")
print s.isNumber("2e10")
