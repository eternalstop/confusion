#!/usr/bin/env python
# encoding: utf-8

import string

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        alpha = string.ascii_uppercase
        cnt = 0
        mmap = {}
        for ap in alpha:
            cnt = cnt + 1
            mmap[ap] = cnt
        result = 0
        for ap in s:
            result = result * 26 + mmap[ap]
        return result


s = Solution()
print s.titleToNumber('A')
print s.titleToNumber('AA')
