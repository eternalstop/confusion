#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positive_nums = []
        zero_nums = []
        negetive_nums = []
        for num in nums:
            if num > 0:
                positive_nums.append(num)
            elif num == 0:
                zero_nums.append(num)
            else:
                negetive_nums.append(num)
        positive_nums = sorted(positive_nums)
        negetive_nums = sorted(negetive_nums)
        possible_results = []
        if len(positive_nums) >= 3:
            possible_results.append(positive_nums[-1] * positive_nums[-2] * positive_nums[-3])
        if len(positive_nums) >= 1 and len(negetive_nums) >= 2:
            possible_results.append(positive_nums[-1] * negetive_nums[0] * negetive_nums[1])
        if len(zero_nums) > 0:
            possible_results.append(0)
        if len(negetive_nums) >= 3:
            possible_results.append(negetive_nums[-1] * negetive_nums[-2] * negetive_nums[-3])
        return max(possible_results)
