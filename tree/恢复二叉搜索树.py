# 题目
# 给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。
# 解题关键：找出排序中错位的两个节点
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    error_node = None
    inoder_prenum = 0
    inorder_prenum_node = None
    error_node2 = None
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.handle(root)
        temp = self.error_node2.val
        self.error_node2.val = self.error_node.val
        self.error_node.val = temp

    def handle(self, root: Optional[TreeNode]) -> None:

        if not root:
            return
        self.handle(root.left)

        if self.error_node and self.inoder_prenum > root.val:
            self.error_node2 = root
        elif not self.error_node and self.inoder_prenum > root.val:
            self.error_node = self.inorder_prenum_node
            self.error_node2 = root
        self.inoder_prenum = root.val
        self.inorder_prenum_node = root
        self.handle(root.right)