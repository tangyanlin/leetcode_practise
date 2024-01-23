class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        def dfs(start, path, target):
            if target == 0: 
                res.append(copy.deepcopy(path[:]))
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    if i>start and candidates[i] == candidates[i-1]: 
                        continue
                    path.append(candidates[i])
                    dfs(i+1, path, target-candidates[i])
                    path.pop()
        start = 0
        path, res = [], []
        candidates.sort()
        dfs(start, path, target)
        return res
