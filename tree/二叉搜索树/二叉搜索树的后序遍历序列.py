def verifyPostorder(self, postorder: List[int]) -> bool:
     if not postorder: return True
     # 找到第一个比root更大的节点i  root=后序最后一个节点
     for i in range(len(postorder)):
         if postorder[i] > postorder[-1]: break
     # i左边是左子树  i右边是右子树
     left = postorder[:i]
     right = postorder[i:-1]
     # 判断左子树是不是都比根节点小 右子树是不是都比根节点大
     for x in left:
         if x > postorder[-1]: return False
     for x in right:
         if x < postorder[-1]: return False
     # 再判断左子树和右子树是否满足条件
     return self.verifyPostorder(left) and self.verifyPostorder(right)
