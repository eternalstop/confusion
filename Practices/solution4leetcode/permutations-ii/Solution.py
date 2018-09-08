#import itertools
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        s = set([])
        for item in itertools.permutations(num):
            s.add(item)
        return [list(item) for item in s]


