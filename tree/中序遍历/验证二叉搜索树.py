# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, min_num, max_num):
            if not root:
                return True
            if root.val <= min_num or root.val >=max_num:
                return False
            return dfs(root.left, min_num, root.val) and dfs(root.right, root.val, max_num)
        
        return dfs(root, float(-inf), float(+inf))

    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = []
        cur = root
        max_num = cur.val
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val <= max_num:
                return False
            else:
                max_num =  cur.val
            cur = cur.right
        return True
            