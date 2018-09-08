#!/usr/bin/env python
# encoding: utf-8


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def walk_tree(self, node):
        if not node:
            return
        self.result.append(str(node.val))
        if not node.left and not node.right:
            return
        self.result.append('(')
        if node.left:
            self.walk_tree(node.left)
        self.result.append(')')
        if node.right:
            self.result.append('(')
            self.walk_tree(node.right)
            self.result.append(')')
        return

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        self.result = []
        self.walk_tree(t)
        return ''.join(self.result)
