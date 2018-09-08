#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        temp = filter(lambda x: x != 0, nums)
        nums[:] = temp + [0] * (length - len(temp))
