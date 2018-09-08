class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        return bin(int(a) + int(b))[2:]


s = Solution()
print(s.addBinary('1', '2'))
