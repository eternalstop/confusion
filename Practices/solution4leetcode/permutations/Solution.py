#import itertools
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        return [list(item) for item in itertools.permutations(num)]

