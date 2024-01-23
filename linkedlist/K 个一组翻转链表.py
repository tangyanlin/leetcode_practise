# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, start, end):
        pre, cur = None, start
        while cur != end:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        dummy = ListNode(-1)
        rear = dummy
        k_start, k_end = head, head
        while k_end:
            for i in range(k):
                if not k_end:  # 不足k步 直接插在尾部
                    rear.next = k_start
                    return dummy.next
                k_end = k_end.next
            # 找到k步 翻转这k步 再尾插到当前链表中
            rear.next = self.reverse(k_start, k_end)
            rear = k_start  # 翻转之后此时末尾节点是k_start
            # 下一组
            k_start = k_end
        return dummy.next
