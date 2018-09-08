# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def __init__(self):
        self.result = []

    def recursive(self, root):
        if root is None:
            return
        self.result.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

    def preorderTraversal(self, root):
        self.recursive(root)
        return self.result

