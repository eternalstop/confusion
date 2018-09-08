#!/usr/bin/env python
# encoding: utf-8

class MinStack:

    def __init__(self):
        self.stack = []
        self.mmin = 0x7fffffff

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if x < self.mmin:
            self.mmin = x

    # @return nothing
    def pop(self):
        if self.stack:
            x = self.stack.pop()
            if x == self.mmin:
                if self.stack:
                    self.mmin = min(self.stack)
                else:
                    self.mmin = 0x7fffffff

    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.mmin

