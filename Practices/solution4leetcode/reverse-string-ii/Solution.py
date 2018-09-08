#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for idx in xrange(0, len(s), 2 * k):
            s[idx:idx + k] = reversed(s[idx:idx + k])
        return "".join(s)
