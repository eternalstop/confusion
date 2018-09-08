#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_set = set(nums)
        disappeared = list(set(range(1, len(nums) + 1)) - nums_set)
        return sorted(disappeared)
