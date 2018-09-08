#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        return str(x) == str(x)[::-1]


