#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        n, res = abs(num), ''
        while n:
            res = str(n % 7) + res
            n /= 7
        return res if num > 0 else '-' + res
