#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = sorted(nums)
        result = 0
        for idx, num in enumerate(temp):
            if idx % 2 == 0:
                result += num
        return result


s = Solution()
num_list = [1, 2, 4, 3]
print(s.arrayPairSum(num_list))
