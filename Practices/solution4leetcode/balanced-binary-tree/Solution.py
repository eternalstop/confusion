#!/usr/bin/env python
# encoding: utf-8

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root is None:
            return True
        lmax = self.max_depth(root.left)
        rmax = self.max_depth(root.right)
        if abs(lmax - rmax) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def max_depth(self, root):
        if root is None:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1
