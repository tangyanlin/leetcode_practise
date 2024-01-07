# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sums = []
        def dfs(root, s):
            s += str(root.val)
            if not root.left and not root.right:
                sums.append(int(s))
            if root.left:
                dfs(root.left, s)
            if root.right:
                dfs(root.right, s)

        if not root:
            return []
        dfs(root, '')
        return sum(sums)