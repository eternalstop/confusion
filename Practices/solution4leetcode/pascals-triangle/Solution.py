#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        ans = []
        curRow = []
        if numRows >= 1:
            curRow = [1]
            ans.append(curRow)
        if numRows >= 2:
            curRow = [1, 1]
            ans.append(curRow)
        if numRows >= 3:
            for row in xrange(3, numRows + 1):
                l = [1]
                for x in xrange(0, len(curRow)-1):
                    l.append(curRow[x] + curRow[x + 1])
                l.append(1)
                curRow = l
                ans.append(curRow)
        return ans

s = Solution()
print s.generate(1)
print s.generate(2)
print s.generate(3)
