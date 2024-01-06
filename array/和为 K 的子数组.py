class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        mapp = {0:1} # k: 前缀和  v: 前缀和为k出现的次数
        pre = 0  # 记录当前前缀和
        for i in range(len(nums)):
            pre += nums[i]
            if pre - k in mapp: res += mapp[pre-k]

            if pre not in mapp: mapp[pre] = 1
            else: mapp[pre] += 1
        return res
