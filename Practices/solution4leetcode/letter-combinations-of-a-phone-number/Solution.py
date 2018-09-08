#import itertools
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        mmap = {
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': [' ']
        }
        digits = list(digits)
        digits = [mmap[item] for item in digits]
        return [''.join(item) for item in itertools.product(*digits)]

s = Solution()

print s.letterCombinations('23')


