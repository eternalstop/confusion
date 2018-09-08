#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # This is a more pythonic but a little slower method
        # return bin(x ^ y).count('1')
        t = x ^ y
        r = 0
        while t:
            if t % 2 == 1:
                r += 1
            t = t >> 1
        return r
