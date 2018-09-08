# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        # s = set([])
        # s.add(hex(id(head)))
        # while head is not None:
        #     if hex(id(head.next)) in s:
        #         return True
        #     s.add(hex(id(head.next)))
        #     head = head.next
        # return False
        fast = head
        slow = head
        while slow is not None and fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return False
            fast = fast.next
            if fast == slow:
                return True
        return False
