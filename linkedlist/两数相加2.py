# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, l1):
        dummy = ListNode(-1)
        p = l1
        while p:
            temp = p.next
            p.next = dummy.next
            dummy.next = p
            p = temp
        return dummy.next
    def add(self, l1, l2):
        dummy = ListNode(-1, l1)
        p, q = l1, l2
        rear = dummy
        while p and q:   # 不考虑进位 直接相加
            p.val += q.val
            rear = p
            p = p.next
            q = q.next
        if q:
            rear.next = q
        pre, cur = dummy.next, dummy.next.next
        while cur:   # 考虑进位
            if pre.val >= 10:
                cur.val += 1
                pre.val %= 10
            pre = cur
            cur = cur.next
        if pre.val >= 10:  # 末位进位
            pre.val %= 10
            pre.next = ListNode(1)
        return dummy.next
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        l1 = self.add(l1, l2)
        return self.reverse(l1)
