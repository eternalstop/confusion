#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min_row = 400000
        min_col = 400000
        if not ops:
            return m * n
        for a, b in ops:
            min_row = min(min_row, a)
            min_col = min(min_col, b)
        return min_row * min_col
