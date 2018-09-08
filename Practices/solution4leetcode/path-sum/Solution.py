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
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        sum -= root.val
        if root.left is None and root.right is None:
            if sum == 0:
                return True
            else:
                return False
        rst = self.hasPathSum(root.left, sum)
        if rst:
            return True
        rst = self.hasPathSum(root.right, sum)
        if rst:
            return True
        return False


