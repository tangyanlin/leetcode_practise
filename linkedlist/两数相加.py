# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        dummy = ListNode(-1, l1)
        rear = dummy
        # 不考虑进位 直接相加
        while p and q:
            p.val += q.val
            rear = p
            p = p.next
            q = q.next
        if q:
            rear.next = q
        # 下面考虑进位
        pre, cur = dummy.next, dummy.next.next
        while cur:
            if pre.val >= 10:
                cur.val += 1
                pre.val %= 10
            pre = cur
            cur = cur.next
        # 考虑末位进位
        if pre.val >= 10:
            pre.val %= 10
            pre.next = ListNode(1)
        return dummy.next
