class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 3: return 1
        dp = [0 for _ in range(n+1)]
        dp[1] = 0
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(i):
                dp[i] = max(dp[i], j*dp[i-j], j*(i-j))
        return dp[-1]