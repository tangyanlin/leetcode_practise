class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 无重复数字 找到所有和为target的不同组合
        # 同一个数字可以无限制重复被选取
        if not candidates: return []
        def dfs(start, path, target):
            if target == 0: 
                res.append(copy.deepcopy(path))
                return

            for i in range(start, len(candidates)):

                if candidates[i] <= target:

                    path.append(candidates[i])

                    dfs(i, path, target-candidates[i])

                    path.pop()
        path, res = [], []

        dfs(0, path, target)
        return res
