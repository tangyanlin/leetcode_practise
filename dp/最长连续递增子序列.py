class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        
        dp = [0 for _ in range(len(nums))]

        dp[0] = 1
        max_num = dp[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
            max_num = max(max_num, dp[i])
        return max_num
