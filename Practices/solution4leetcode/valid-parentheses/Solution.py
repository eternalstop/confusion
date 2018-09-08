class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                t = stack.pop()
                if s[i] == ')' and t != '(': return False
                if s[i] == ']' and t != '[': return False
                if s[i] == '}' and t != '{': return False
            i += 1
        if len(stack) != 0:
            return False
        return True


