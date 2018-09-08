#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        temp = []
        for t in nums:
            temp += t
        results = [temp[idx: idx + c] for idx in range(0, len(temp), c)]
        return results
