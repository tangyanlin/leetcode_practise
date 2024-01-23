# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainningPlan(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        last = self.trainningPlan(head.next)
        head.next.next = head
        head.next = None
        return last

    #非递归写法
    def reverseList(self, head: ListNode) -> ListNode:
        # 头插法
        # p 当前指针，dummy 倒转后链表的新head，
        dummy = ListNode(-1)
        p = head
        while p:
            temp = p.next
            p.next = dummy.next
            dummy.next = p 
            p = temp
        return dummy.next