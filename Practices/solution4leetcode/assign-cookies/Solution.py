#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        cookies = len(s)
        assign = 0
        for child in g:
            if not s:
                break
            while s:
                if s[0] >= child:
                    assign += 1
                    s.pop(0)
                    break
                s.pop(0)
        return assign
