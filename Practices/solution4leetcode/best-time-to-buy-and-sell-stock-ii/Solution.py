class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        prices = [prices[index + 1] - prices[index] for index, num in enumerate(prices) if index + 1 < len(prices)]
        result = 0
        for item in prices:
            if item > 0:
                result += item
        return result

s = Solution()

print s.maxProfit([])
