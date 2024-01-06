class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if len(coins) == 0:
            return 0
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                if j >= coins[i]:
                    dp[j] = dp[j-coins[i]] + dp[j]
        return dp[-1]