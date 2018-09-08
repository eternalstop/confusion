#!/usr/bin/env python
# encoding: utf-8

from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = dict(Counter(s))
        max_length = 0
        flag = False
        for k, v in counter.iteritems():
            if v == 1:
                flag = True
            elif v % 2 == 0:
                max_length += v
            else:
                flag = True
                max_length += v - 1
        if flag:
            return max_length + 1
        else:
            return max_length
