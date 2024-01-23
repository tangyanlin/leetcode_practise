# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# a+b
# f= 2s; f = s+ nb ==> s = nb, f=2nb ==> k = a+nb ,  slow走了nb步，再走a步即可到达环形第一个节点，a=从head走到环形第一个节点
# 

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head
        while fast:
            slow = slow.next
            if not fast.next:
                return False
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        