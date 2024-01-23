class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp_arr = []
            j = 1
            while j**2 <= i:
                dp_arr.append(dp[i-j**2]+1)
                j += 1
            dp[i] = min(dp_arr)
        return dp[n]