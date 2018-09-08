#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = 1
        while temp <= num:
            temp <<= 1
        temp -= 1
        return temp - num
