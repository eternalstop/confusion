class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = s.strip().split()
        words = reversed(words)
        return ' '.join(words)

