#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        A = 0
        L = 0
        for record in s:
            if record == 'L':
                L += 1
            else:
                if L > 2:
                    return False
                L = 0
            if record == 'A':
                A += 1
            if A > 1:
                return False
        if L > 2:
            return False
        return True
