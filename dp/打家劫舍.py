from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        # dp[i]表示前i家能抢的最高金额
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # 1、不抢第i家 那么前i家抢的最高金额=前i-1抢的最高金额
            # 2、抢第i家，那么前i家抢的最高金额=前i-1家抢的最高金额+第i家的金额
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]


