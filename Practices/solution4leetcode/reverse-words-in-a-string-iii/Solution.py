#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(map(lambda x: x[::-1], s.split()))
