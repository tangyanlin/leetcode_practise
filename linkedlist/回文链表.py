# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        stack = []
        slow, fast = head, head
        # 把前面一半的节点值存入栈中 
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        # 链表有奇数个节点 中间奇数位不需要比较 slow向后移一位
        if fast: slow = slow.next
        while slow:
            # 后一半节点一个个的和栈顶元素比较
            if slow.val != stack.pop():
                return False
            slow = slow.next
        return True
