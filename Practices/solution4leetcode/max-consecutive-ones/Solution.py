#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        max_result = 0
        for num in nums:
            if num == 0:
                max_result = max(max_result, result)
                result = 0
            else:
                result += 1
        max_result = max(max_result, result)
        return max_result
