#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        new_tail = ListNode(head.val)
        node = head.next
        while node:
            new_node = ListNode(node.val)
            new_node.next = new_tail
            new_tail = new_node
            node = node.next
        return new_tail
