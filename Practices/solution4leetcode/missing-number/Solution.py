#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        return len(nums) * (len(nums) + 1) / 2 - total_sum
