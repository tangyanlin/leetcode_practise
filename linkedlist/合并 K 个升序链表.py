# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: return
        if len(lists) == 1: return lists[0] 
        dummy = ListNode(-1)
        rear = dummy
        heap = []
        # 存储lists中所有链表的第一个节点值以及对应的链表idx
        for idx in range(len(lists)):
            if lists[idx]:
                # lists[idx]存放的是第idx个链表的head节点
                heapq.heappush(heap, (lists[idx].val, idx))  
                lists[idx] = lists[idx].next
        while heap:
            # pop出堆顶元素  最小值,链表idx
            min_val, idx = heapq.heappop(heap)
            # 将最小值接到最终链表尾部
            rear.next = ListNode(min_val)
            rear = rear.next
            # 如果这个idx链表不为空，再从这个链表中取出最小值 放入堆中
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next  # 头节点向后移一位
        return dummy.next
