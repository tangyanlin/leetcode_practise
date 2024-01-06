# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        dummy = ListNode(-1, head)
        pre, cur = dummy, head
        # 注意这里的cur and cur.next和cur.next and cur是不一样的
        # 加入cur是因为下面的特殊情况[1,2,3,3,3] 最后cur=None 这里的while就会报错
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.val == cur.next.val:
                    cur = cur.next
                    # 特殊情况 [1,2,3,3,3] 到最后cur.next=None 报错
                    if not cur.next: break 
                pre.next = cur.next
                cur = pre.next
            else:
                pre, cur = cur, cur.next
        return dummy.next
