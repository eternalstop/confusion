#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        ans = [0] * (rowIndex + 1)
        ans[0] = 1
        for i in xrange(1, rowIndex + 1):
            ans[i] = 1
            for j in xrange(i-1, 0, -1):
                ans[j] = ans[j] + ans[j-1]
        return ans

s = Solution()
print s.getRow(3)
