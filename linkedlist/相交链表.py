# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        p, q = headA, headB
        while p != q:
            p = headB if not p else p.next
            q = headA if not q else q.next
        return p
