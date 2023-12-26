class Solution:
    def helper(self, nums: List[int]) -> int:
        # 正常数组：LeetCode198. 打家劫舍
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        # 不抢头 不抢尾
        nums1 = self.helper(nums[1:-1])
        # 不抢头 抢尾
        nums2 = self.helper(nums[1:])
        # 抢头 不抢尾
        nums3 = self.helper(nums[:-1])
        return max(nums1, nums2, nums3)
