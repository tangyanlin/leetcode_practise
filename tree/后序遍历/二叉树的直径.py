# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        self.max_count = 1  # 最大节点个数
        def dfs(root):
            # 函数返回：以root为根节点这颗树的最大直径
            # 递归出口
            if not root: return 0
            # 左子树最大节点个数
            left = dfs(root.left)
            # 右子树最大节点个数
            right = dfs(root.right)
            # 当前层逻辑
            # root这颗树的最大节点个数=左子树最大节点个数+右子树最大节点个数+1
            self.max_count = max(self.max_count, left+right+1) 
            # 往上走root作为子树的最大节点个数
            return max(left, right) + 1
        dfs(root)
        return self.max_count - 1  # 最大直径
