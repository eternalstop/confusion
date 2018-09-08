#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        return str(bin(n)).count('1')
