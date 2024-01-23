def serialize(self, root):
    """Encodes a tree to a single string. 
    前序遍历
    :type root: TreeNode
    :rtype: str
    """
    self.res = []
    def dfs(root):
        if not root: self.res.append('#')
        else:
            self.res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
    dfs(root)
    return ' '.join(self.res)  # str    1 2 # # 3 4 # # 5 # #

def deserialize(self, data):
    """Decodes your encoded data to tree.
    :type data: str
    :rtype: TreeNode
    """
    data = list(data.split(" "))  # ['1', '2', '#', '#', '3', '4', '#', '#', '5', '#', '#']
    def dfs():
        if data[0] == '#':
            data.pop(0)
            return None
        else:
            cur = TreeNode(data.pop(0))
            cur.left = dfs()
            cur.right = dfs()
            return cur
    return dfs()