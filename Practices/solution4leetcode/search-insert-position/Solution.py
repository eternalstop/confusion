class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        left = 0
        high = len(A)
        while left < high:
            mid = (left + high) // 2
            if A[mid] < target: left = mid+1
            else: high = mid
        return left

