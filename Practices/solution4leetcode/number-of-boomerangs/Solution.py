#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        for point_i in points:
            dis_map = {}
            for point_j in points:
                if point_i == point_j:
                    continue
                dis = (point_i[0] - point_j[0]) ** 2 + (point_i[1] - point_j[1]) ** 2
                if dis in dis_map:
                    dis_map[dis] += 1
                else:
                    dis_map[dis] = 1
            for k, v in dis_map.iteritems():
                if v >= 2:
                    result += v * (v - 1)
        return result
