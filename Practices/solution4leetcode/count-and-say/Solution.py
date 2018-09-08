#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @return a string
    def countAndSay(self, n):
        ans = "1"
        for i in xrange(2, n + 1):
            a = []
            l = list(ans)
            length = len(l)
            num = 1
            for idx in xrange(1, length):
                if l[idx] == l[idx-1]:
                    num = num + 1
                else:
                    a.append(str(num))
                    a.append(l[idx-1])
                    num = 1
            a.append(str(num))
            a.append(l[length-1])
            ans = ''.join(a)
        return ans

