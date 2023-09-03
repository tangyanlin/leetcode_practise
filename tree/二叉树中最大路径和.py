# 题目
# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

# 路径和 是路径中各节点值的总和。

# 给你一个二叉树的根节点 root ，返回其 最大路径和 。

#解题关键：搞清楚节点向上传递的可用最大值和全局最大值的差别即可
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_num = -1001

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.handle(root)
        return self.max_num
        
    def handle(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        value = root.val
        leftnum = -1001
        rightnum = -1001
        if root.left:
            leftnum = self.handle(root.left)
        if root.right:
            rightnum = self.handle(root.right)
        temp_max_num = max([leftnum, leftnum + value, leftnum + value + rightnum, rightnum, value, value+rightnum])
        if temp_max_num > self.max_num:
            self.max_num = temp_max_num
        return max([leftnum + value, value, value+rightnum])