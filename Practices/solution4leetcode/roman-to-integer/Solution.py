class Solution:
    # @return an integer
    def romanToInt(self, s):
        r2n = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        s = list(s)
        ret = 0
        for i, c in enumerate(s):
            if i > 0 and r2n[s[i]] > r2n[s[i-1]]:
                ret += r2n[s[i]] - r2n[s[i-1]] * 2
            else:
                ret += r2n[s[i]]
        return ret



s = Solution()
print s.romanToInt("XXX")
