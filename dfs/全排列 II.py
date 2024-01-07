class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 包含重复数字的全排列
        if not nums: return []
        def dfs(path, res, nums, used):
            if len(path) == len(nums):
                res.append(copy.deepcopy(path))
                return
            for i in range(len(nums)):
                if used[i] == True:
                    continue
                if i>0 and nums[i]==nums[i-1] and used[i-1] == True:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs(path, res, nums, used)
                path.pop()
                used[i] = False
        path, res = [], []
        # 注意这里的去重为什么用False这种形式 而不用set集合记录的形式
        # 因为这里的序列是可能有重复数字的 并不唯一 所以数字是不能代表某个位置数的
        used = [False for _ in range(len(nums))]
        nums.sort()
        dfs(path, res, nums, used)
        return res
