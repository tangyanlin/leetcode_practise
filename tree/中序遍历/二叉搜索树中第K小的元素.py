class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root or k < 0: return -1
        stack, cur = [], root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0: return cur.val
            cur = cur.right
