# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 求以root为根节点的树里节点值之和等于targetSum的路径个数 
        if not root: return 0
        def dfs(node, cur_sum):
            # 以node为根节点的的树里节点值之和等于targetSum且起始节点为node的路径个数
            # 递归出口 
            if not node: return 0
            res = 0
            # 处理当前层逻辑
            if node.val == cur_sum: 
                res += 1
            res += dfs(node.left, cur_sum-node.val)
            res += dfs(node.right, cur_sum-node.val)
            return res
        res = dfs(root, targetSum)
        res += self.pathSum(root.left, targetSum)
        res += self.pathSum(root.right, targetSum)
        return res
