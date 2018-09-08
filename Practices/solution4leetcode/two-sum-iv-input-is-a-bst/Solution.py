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
        if root:
            self.numbers.add(root.val)
            self.walk_tree(root.left)
            self.walk_tree(root.right)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.numbers = set()
        self.walk_tree(root)
        for val in self.numbers:
            other = k - val
            if other == val:
                continue
            if other in self.numbers:
                return True
        return False
