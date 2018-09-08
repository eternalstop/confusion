#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        l = []
        for ch in s.lower():
            if str(ch).isalnum():
                l.append(ch)
        ss = ''.join(l)
        if ss == ss[::-1]:
            return True
        else:
            return False

s = Solution()
print s.isPalindrome('1a2')
