#!/usr/bin/env python
# encoding: utf-8


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def walk_tree(self, root, direction):
        if not root:
            return
        if not root.left and not root.right and direction == 'left':
            self.result += root.val
        self.walk_tree(root.left, 'left')
        self.walk_tree(root.right, 'right')

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.walk_tree(root, 'None')
        return self.result
