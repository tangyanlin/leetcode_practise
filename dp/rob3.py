# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root: return 0
        def robTree(root):
            if not root: return [0, 0]
            left = robTree(root.left)
            right = robTree(root.right)

            # 如果不偷当前层root 那么考虑左右孩子
            # 返回左孩子最大偷窃金额+右孩子最大偷窃金额
            val1 = max(left) + max(right)
            # 如果偷当前层root 那么左右孩子都不能偷
            val2 = root.val + left[0] + right[0]
            # [不偷当前节点最终偷到的最大金额, 偷当前节点最终偷到的最大金额]
            return [val1, val2]
        return max(robTree(root))
