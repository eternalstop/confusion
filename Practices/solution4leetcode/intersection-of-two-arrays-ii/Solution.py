#!/usr/bin/env python
# encoding: utf-8

from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        results = []
        for x in c1:
            if x not in c2:
                continue
            smaller = min(c1[x], c2[x])
            results += [x] * smaller
        return results
