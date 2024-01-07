# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.max_path_sum = float('-inf')
        def dfs(root):
            # 函数返回：以root为根节点的这棵树的最大路径和  
            # 注意返回root这课树的最大路径和它必须是向上的  也就是只能选择左子树或者右子树其中一个
            # 如果都是选的话 那么这棵树就是横向的了
            # 递归出口
            if not root: return 0
            # 调用左子树 求左子树最大路径和
            left = max(dfs(root.left), 0)
            # 调用右子树 求右子树最大路径和
            right = max(dfs(root.right), 0)
            # 更新整棵树的最大路径和
            self.max_path_sum = max(self.max_path_sum, left+right+root.val)
            # 处理当前节点 向上返回 以root为根节点的最大路径和=max(左，右)+root
            return max(left, right) + root.val
        dfs(root)
        return self.max_path_sum