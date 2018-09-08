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
            self.walk_tree(root.right)
            self.part_sum += root.val
            root.val = self.part_sum
            self.walk_tree(root.left)
            return root.val
        return 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.part_sum = 0
        self.walk_tree(root)
        return root
