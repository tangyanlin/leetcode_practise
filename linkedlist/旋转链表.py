# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        slow = head
        fast = head
        lengh = 0
        p =head
        while p:
            lengh +=1
            p= p.next
        if lengh == 0:
            return head

        if k >= lengh:
            k = k%lengh
        if not head or not head.next or k ==0:
            return head
        for i in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head