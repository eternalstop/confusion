#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        t = bin(n)[2:]
        return int(('0' * (32 - len(t)) + t)[::-1], 2)

