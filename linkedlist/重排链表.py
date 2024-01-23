# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        dummy = ListNode(-1)
        p = head
        while p:
            temp = p.next
            p.next = dummy.next
            dummy.next = p
            p = temp
        return dummy.next
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next: return head
        # 找中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 中间切断
        new_head = slow.next
        slow.next = None
        # 后半部分逆序
        new_head = self.reverse(new_head)
        # 交叉插入新链表中
        dummy = ListNode(-1)
        rear = dummy
        p, q = head, new_head
        while p and q:
            rear.next = p
            rear = p
            p = p.next
            
            rear.next = q
            rear = q
            q = q.next
        rear.next = p if p else q
        return dummy.next
