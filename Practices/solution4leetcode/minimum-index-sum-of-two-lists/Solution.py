#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        list1_dict = {x: idx for idx, x in enumerate(list1)}
        list2_dict = {x: idx for idx, x in enumerate(list2)}
        minimum_index_sum = 20000
        result = []
        for key, val in list1_dict.iteritems():
            if key in list2_dict:
                if minimum_index_sum > val + list2_dict[key]:
                    minimum_index_sum = val + list2_dict[key]
                    result = [key]
                elif minimum_index_sum == val + list2_dict[key]:
                    result.append(key)
        return result
