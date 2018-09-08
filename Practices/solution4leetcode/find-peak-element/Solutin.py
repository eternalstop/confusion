#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        length = len(num)
        return self.find(0, length - 1, num)

    def find(self, left, right, num):
        if left == right:
            return left
        if left + 1 == right:
            return [left, right][num[left] < num[right]]
        mid = (left + right) / 2
        if num[mid] < num[mid + 1]:
            return self.find(mid + 1, right, num)
        if num[mid] < num[mid - 1]:
            return self.find(left, mid - 1, num)
        return mid


s = Solution()
print s.findPeakElement([1, 2])
