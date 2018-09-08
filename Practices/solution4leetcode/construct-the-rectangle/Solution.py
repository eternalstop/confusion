#!/usr/bin/env python
# encoding: utf-8


import math


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        l, w = area, 1
        W = int(math.floor(math.sqrt(area)))
        while W > 1:
            if area % W == 0:
                l, w = area / W, W
                break
            W -= 1
        return [l, w]
