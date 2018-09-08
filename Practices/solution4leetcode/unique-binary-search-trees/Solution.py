def catalan(n):
    if n <= 2:
        return n
    return (2 * n) * (2 * n - 1) * catalan(n - 1) / ((n + 1) * n)

class Solution:
    # @return an integer
    def numTrees(self, n):
        return catalan(n)

s = Solution()
print s.numTrees(3)

