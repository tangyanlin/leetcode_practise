class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 无重复数字 找到所有和为target的不同组合
        # 同一个数字可以无限制重复被选取
        if not candidates: return []
        def dfs(start, path, res, candidates, target):
            if target == 0: 
                res.append(copy.deepcopy(path))
                return
            # 这里不加start的话就会每次都从头遍历 start就保证每次都从start位置开始遍历
            # 就会出现223 232的情况 就会重复了
            for i in range(start, len(candidates)):
                # 剪枝 小于target就不用进去了  因为target-candidates[i]肯定不等于0
                if candidates[i] <= target:
                    # 设置现场
                    path.append(candidates[i])
                    # 下一层的start=i 说明当前数字在后面dfs时还可以使用 允许一个数字重复使用
                    # 如 223  
                    dfs(i, path, res, candidates, target-candidates[i])
                    # 恢复现场
                    path.pop()
        path, res = [], []
        # candidates.sort()  没有重复数字 不用sort
        dfs(0, path, res, candidates, target)
        return res
