def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root: return []
    res, queue = [], [root]
    i = 0
    while queue:
        arr, size = [], len(queue)
        for _ in range(size):
            cur = queue.pop(0)
            arr.append(cur.val)
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)
        if i % 2 == 0: res.append(arr)  # 偶数行正序 
        else: res.append(arr[::-1])     # 奇数行逆序
        i += 1
    return res
