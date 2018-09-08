#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    @staticmethod
    def addDigits(num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        r = num % 9
        return r if r else 9


s = Solution()
print(s.addDigits(18))
