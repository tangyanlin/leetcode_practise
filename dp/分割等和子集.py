class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        bag_weight = s//2

        dp = [[0 for _ in range(bag_weight+1)]for _ in range(len(nums)+1)]

        for i in range(len(nums)):
            for j  in range(1, bag_weight+1):
                if j - nums[i] >= 0:
                    dp[i][j] = max([dp[i-1][j - nums[i]] + nums[i], dp[i-1][j]])
                else:
                    dp[i][j] = dp[i-1][j]
                if dp[i][j] == bag_weight:
                    return True
        return False
    
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        bag_weight = s//2

        dp = [0 for _ in range(bag_weight+1)]

        for i in range(len(nums)):
            for j  in range(bag_weight, nums[i]-1, 1):
                if j - nums[i] >= 0:
                    dp[j] = max([dp[j - nums[i]] + nums[i], dp[j]])
                if dp[j] == bag_weight:
                    return True
        return False