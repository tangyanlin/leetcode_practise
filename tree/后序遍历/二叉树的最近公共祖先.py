# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': 
        # 典型的后序遍历
        # 函数返回：当前以root节点为根节点的树p或q的最近公共祖先
        # 递归出口1 空树了就不需要继续找了
        if not root: return None
        # 递归出口2 当前节点是p或者q 返回root 
        if root == p or root == q: return root
        # 去左右子树找p和q的最近公共祖先
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 处理当前节点的逻辑
        # 如果都不为空 那么root就是p和q的最近公共祖先
        if left and right: return root
        # 都为空 就返回None
        elif not left and not right: return None
        # left不为空  pq都在left 返回left
        # left为空    pq都在right 返回right
        else: return left if left else right  