class Solution:
    # @return an integer
    def reverse(self, x):
        if x > 0:
            return int(''.join(list(str(x))[::-1]))
        else:
            return -int(''.join(list(str(-x))[::-1]))

s = Solution()
print s.reverse(10000000000000003)
print s.reverse(0)
print s.reverse(-1000000002)
