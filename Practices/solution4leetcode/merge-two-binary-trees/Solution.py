#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        result_tree = None
        if t1 and t2:
            result_tree = TreeNode(t1.val + t2.val)
            result_tree.left = self.mergeTrees(t1.left, t2.left)
            result_tree.right = self.mergeTrees(t1.right, t2.right)
        elif t1 and not t2:
            result_tree = TreeNode(t1.val)
            result_tree.left = t1.left
            result_tree.right = t1.right
        elif not t1 and t2:
            result_tree = TreeNode(t2.val)
            result_tree.left = t2.left
            result_tree.right = t2.right
        return result_tree
        