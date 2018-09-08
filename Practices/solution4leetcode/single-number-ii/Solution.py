class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        tmp = {}
        for item in A:
            if item in tmp:
                tmp[item] += 1
            else:
                tmp[item] = 1
        for k in tmp:
            if tmp[k] == 1:
                return k


