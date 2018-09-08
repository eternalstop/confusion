class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        dp = [0 for _ in range(n+2)]
        dp[1] = 1
        dp[2] = 2
        i = 3
        while i <= n:
            dp[i] = dp[i-1] + dp[i-2]
            i += 1
        return dp[n]

s = Solution()
print s.climbStairs(3)


