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
            return
        self.walk_tree(root.left)
        self.values.append(root.val)
        self.walk_tree(root.right)

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.values = []
        self.walk_tree(root)
        return min([y - x for x, y in zip(self.values, self.values[1:])])
