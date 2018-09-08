#!/usr/bin/env python
# encoding: utf-8


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def walk_tree(self, root):
        if not root:
            return 0
        sum_left = self.walk_tree(root.left)
        sum_right = self.walk_tree(root.right)
        self.tilt += abs(sum_left - sum_right)
        return root.val + sum_left + sum_right

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt = 0
        self.walk_tree(root)
        return self.tilt
