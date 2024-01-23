def largestValues(self, root: TreeNode) -> List[int]:
    if not root: return []
    res, queue = [], [root]
    while queue:
        size = len(queue)
        for i in range(size):
            # 这里也可以写arr 后面再用max(arr),但是这里为了节省空间 空间复杂度为O(1)
            if i == 0: max_val = float('-inf')
            cur = queue.pop(0)
            max_val = max(max_val, cur.val)
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)
        res.append(max_val)
    return res
