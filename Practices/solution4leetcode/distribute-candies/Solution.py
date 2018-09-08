#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        total_num = len(candies)
        uniq_num = len(set(candies))
        return uniq_num if uniq_num * 2 <= total_num else total_num / 2
