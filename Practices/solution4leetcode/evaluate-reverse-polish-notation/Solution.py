class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        operations = {
            '+': lambda x, y: int(float(x) + float(y)),
            '-': lambda x, y: int(float(x) - float(y)),
            '*': lambda x, y: int(float(x) * float(y)),
            '/': lambda x, y: int(float(x) / float(y)),
        }
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                result = operations[token](b, a)
                stack.append(result)

        return stack.pop()

