# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1, head)
        slow, fast = dummy, head
        for i in range(n):  # 快指针往前走n步
            fast = fast.next
        while fast:  # 快慢指针一起走
            fast = fast.next
            slow = slow.next
        # 快指针走向链表外 慢指针刚好走到倒数第n个节点的前一个节点
        slow.next = slow.next.next
        return dummy.next
