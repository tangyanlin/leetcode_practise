# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.flag = False
        def dfs(root, targetSum): 
            if self.flag:
                return
            if root:
                targetSum -= root.val
            if not root.left and not root.right and targetSum == 0:
                self.flag = True
            if root.left:
                dfs(root.left, targetSum)
            if root.right:
                dfs(root.right, targetSum)
        if not root:
            return self.flag
        dfs(root, targetSum)
        return self.flag
        

