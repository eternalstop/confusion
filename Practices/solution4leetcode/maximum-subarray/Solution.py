class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if A:
            heresum = maxsum = A[0]
            for num in A[1:]:
                if heresum <= 0:
                    heresum = num
                else:
                    heresum += num
                if heresum > maxsum:
                    maxsum = heresum
            return maxsum
        return 0

