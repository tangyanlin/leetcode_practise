# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, left, right):
        dummy = ListNode(-1)
        rear = dummy
        p, q = left, right
        while p and q:
            if p.val <= q.val:
                rear.next = p
                p = p.next
            else:
                rear.next = q
                q = q.next
            rear = rear.next
        rear.next = p if p else q
        return dummy.next 
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        # 找到链表中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 偶数个节点 fast=链表最后一个节点 slow指向前半部分节点的最后一个
        # 奇数个节点 fast=null slow指向中间节点

        # 把链表切成两部分，再对这俩个部分进行排序
        mid = slow.next
        slow.next = None
        left, right = self.sortList(head), self.sortList(mid)

        # 最后将两个排序链表合并为一个有序链表
        return self.merge(left, right)
