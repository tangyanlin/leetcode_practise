class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        def dfs(start, path, res, candidates, target):
            if target == 0: 
                res.append(copy.deepcopy(path[:]))
                return   # 不需要再向下找了
                # start防止出现116 161的现象
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                # 一个数字在一个组合当中只能使用一次，所以i不能进入dfs 
                # 否则同一个数就在这个组合当中出现两次了
                # 防止出现112的情况
                    if i>start and candidates[i] == candidates[i-1]: 
                        continue
                    path.append(candidates[i])
                # dfs的循环内是在一个组合
                # 当前数字只能用一次（每个数字在每个组合中只能使用一次） 后面dfs不能使用 
                # 防止出现225的情况
                    dfs(i+1, path, res, candidates, target-candidates[i])
                    path.pop()
        start = 0
        path, res = [], []
        # 这种集合中有重复数字都要sort
        candidates.sort()
        dfs(start, path, res, candidates, target)
        return res
