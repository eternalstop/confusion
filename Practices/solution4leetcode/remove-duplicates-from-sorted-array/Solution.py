#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 2:
            return len(A)
        i = 1
        j = 0
        while i < len(A):
            if A[i] == A[j]:
                i += 1
            else:
                j += 1
                A[j] = A[i]
                i += 1
        return j+1

