class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        if len(coins) == 0: return -1
        # dp[i]表示抽成总金额为i的最少金币数
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] = min(dp[j], dp[j-coins[i]]+1)
        return dp[-1] if dp[-1] != float('inf') else -1
