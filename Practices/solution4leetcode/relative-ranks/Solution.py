#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums2 = sorted(nums, reverse=True)
        nums_dict = {val: idx + 1 for idx, val in enumerate(nums2)}
        result = []
        for score in nums:
            rank = nums_dict[score]
            if rank == 1:
                result.append('Gold Medal')
            elif rank == 2:
                result.append('Silver Medal')
            elif rank == 3:
                result.append('Bronze Medal')
            else:
                result.append(str(rank))
        return result
