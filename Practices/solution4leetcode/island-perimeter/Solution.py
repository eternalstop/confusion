#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid[0])
        row_num = len(grid)
        new_grid = [[0] * (length + 1)]
        for row in grid:
            new_grid.append([0] + row + [0])
        new_grid.append([0] * (length + 1))
        result = 0
        for i in range(1, row_num + 1):
            for j in range(1, length + 1):
                if new_grid[i][j] == 0:
                    continue
                if new_grid[i][j - 1] == 0:
                    result += 1
                if new_grid[i - 1][j] == 0:
                    result += 1
                if new_grid[i][j + 1] == 0:
                    result += 1
                if new_grid[i + 1][j] == 0:
                    result += 1
        return result
