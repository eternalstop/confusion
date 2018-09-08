#!/usr/bin/env python
# encoding: utf-8

# fuck the leetcode test case
# if you only use Python
# you will alway get
# Output:"e" Expected:'e'
# you must change language to Python3


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sl = sorted(s)
        tl = sorted(t)
        sl.append('$')
        for x, y in zip(sl, tl):
            if x != y:
                return y
