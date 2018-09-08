#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = {num: idx for idx, num in enumerate(nums)}
        result = []
        for x in findNums:
            idx = temp[x]
            for num in nums[idx + 1:]:
                if num > x:
                    result.append(num)
                    break
            else:
                result.append(-1)
        return result
