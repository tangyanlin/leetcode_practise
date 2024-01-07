# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.paths = []
        def dfs(root, targetSum, path): 
            if root:
                targetSum -= root.val
                path.append(root.val)
            if not root.left and not root.right and targetSum == 0:
                self.paths.append(path.copy())
            if root.left:
                dfs(root.left, targetSum, path)
            if root.right:
                dfs(root.right, targetSum, path)
            path.pop()
        if not root:
            return []
        dfs(root, targetSum, [])
        return self.paths