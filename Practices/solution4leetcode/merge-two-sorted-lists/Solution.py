# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1 and not l2:
            return l1
        if not l1:
            return l2
        if not l2:
            return l1
        lan = []
        lan.append(l1.val)
        while l1.next:
            l1 = l1.next
            lan.append(l1.val)
        lan.append(l2.val)
        while l2.next:
            l2 = l2.next
            lan.append(l2.val)
        lan.sort()
        head = ListNode(lan[0])
        p = head
        for item in lan[1:]:
            node = ListNode(item)
            p.next = node
            p = p.next
        return head


