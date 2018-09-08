#!/usr/bin/env python
# encoding: utf-8


import string


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        init_map = {s: [] for s in string.lowercase}
        for idx, char in enumerate(s):
            init_map[char].append(idx)
        for char in s:
            if len(init_map[char]) == 1:
                return init_map[char][0]
        return -1
