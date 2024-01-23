class Solution:
     def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        def dfs(start, path):
            if len(path) >= 2:
                res.append(copy.deepcopy(path))
                # 注意这里没有return了 因为子序列还可以继续向下找
            used = []  # 每一层都有一个used
            for i in range(start, len(nums)):
                # 去重操作 这里不能和子集一样sort 子序列要求是不能改变原始的相对位置
                # 所以这里用一个set来存放当前层已经用过哪些元素
                # 第二个条件保证递增
                if nums[i] in used or (len(path)>0 and path[-1]>nums[i]): continue 
                path.append(nums[i])
                used.append(nums[i])
                dfs(i+1, path)
                path.pop()
        start = 0
        path, res = [], []
        dfs(start, path)
        return res
