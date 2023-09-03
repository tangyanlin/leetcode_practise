# 题目
# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
# 解题关键：从拆解数组长度角度出发
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build_node(preorder, inorder)

    
    def build_node(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not inorder:
            return None
        root_value = preorder[0]
        
        root_inorder_index = inorder.index(root_value)
        left_num = root_inorder_index
        right_num = len(inorder) - root_inorder_index - 1

        left = self.build_node(preorder[1: 1+left_num], inorder[0:left_num])
        right = self.build_node(preorder[left_num+1: len(preorder)], inorder[left_num+1:len(inorder)])
        return TreeNode(root_value, left, right)