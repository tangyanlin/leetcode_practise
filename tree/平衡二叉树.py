# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def dfs(root):
            # 函数返回：以root为根节点的这棵树是否是平衡二叉树
            # 递归出口
            if not root: return 0
            # 边求高度边判断
            left = dfs(root.left)
            # 如果当前节点左子树不是平衡二叉树 那么以当前节点为根节点的树也不是平衡二叉树
            if left == -1: return -1
            # 如果当前节点右子树不是平衡二叉树 那么以当前节点为根节点的树也不是平衡二叉树
            right = dfs(root.right)
            if right == -1: return -1
            # 左右子树都是平衡二叉树 再判断当前节点是不是平衡二叉树 如果是的话返回-1
            # 不是的话返回以当前节点为根节点的子树高度
            # 当前层逻辑
            return max(left, right)+1 if abs(left-right)<=1 else -1
        return dfs(root) != -1
