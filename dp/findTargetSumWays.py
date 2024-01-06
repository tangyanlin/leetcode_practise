class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 设数组中添加'-'元素的总和为neg  则添加'+'的总和为sum_nums-neg
        # (sum_nums-neg) - neg = target => bagweight = neg = (sum_nums-target)//2
        # 所以问题转换为：求出和为bagweight的个数
        sum_nums = sum(nums)
        if (sum_nums - target) % 2 == 1: return 0
        if target > sum_nums: return 0
        bagweight = (sum_nums - target) // 2
        dp = [0 for _ in range(bagweight + 1)]
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bagweight, nums[i]-1, -1):
                if j >= nums[i]:
                    dp[j] += dp[j-nums[i]]
        return dp[-1]
