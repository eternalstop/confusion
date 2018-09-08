#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return sum(nums) - nums[0] * len(nums)
