# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTargetNode(self, root: Optional[TreeNode], cnt: int) -> int:
        stack, cur = [], root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cnt -= 1
            if cnt == 0: return cur.val
            cur = cur.left