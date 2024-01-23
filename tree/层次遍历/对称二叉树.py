def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root: return True
    queue = [root]
    while queue:
        arr, size = [], len(queue)
        for i in range(size):
            cur = queue.pop(0)
            # 这里如果出现空 就加入‘#’
            if not cur: arr.append('#')
            else: arr.append(cur.val)
            if cur:
                queue.append(cur.left)
                queue.append(cur.right)
        if arr != arr[::-1]: return False
    return True 
