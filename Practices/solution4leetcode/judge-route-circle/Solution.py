#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        original_x = 0
        original_y = 0
        for move in moves:
            if move == 'L':
                original_x -= 1
            elif move == 'R':
                original_x += 1
            elif move == 'U':
                original_y += 1
            elif move == 'D':
                original_y -= 1
        if original_x == 0 and original_y == 0:
            return True
        return False
