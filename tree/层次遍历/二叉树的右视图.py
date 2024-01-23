def rightSideView(self, root: TreeNode) -> List[int]:
    if not root: return []
    res, queue = [], [root]
    while queue:
        size = len(queue)
        for i in range(size):
            cur = queue.pop(0)
            if i == (size-1):
                res.append(cur.val)
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)
    return res
