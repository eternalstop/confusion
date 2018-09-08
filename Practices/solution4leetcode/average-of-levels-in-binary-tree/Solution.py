#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def get_struct(self, node, deepth, struct):
        if len(struct) <= deepth:
            struct.append([])
        struct[deepth].append(node.val)
        if node.left:
            self.get_struct(node.left, deepth + 1, struct)
        if node.right:
            self.get_struct(node.right, deepth + 1, struct)

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        struct = []
        self.get_struct(root, 0, struct)
        result = []
        for part in struct:
            result.append(sum(part) / float(len(part)))
        return result
