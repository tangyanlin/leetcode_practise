class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 不包含重复数字的全排列
        if not nums: return []
        # 用used来全场记录我当前的排列用到了哪些元素  
        # 如果用了的话就continue 因为排列是不能重复的
        def dfs(path):
            if len(path) == len(nums):
                res.append(copy.deepcopy(path))
                return
            for i in range(len(nums)):
                if nums[i] in path: continue
                path.append(nums[i])
                dfs(path)
                path.pop()
        path, res = [], []
        dfs(path)
        return res
