class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) < 1:
            return 0
        if len(grid[0]) < 1:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n+2)] for _ in range(m+2)]

        for i in range(n, 0, -1):
            dp[m][i] = dp[m][i+1] + grid[m-1][i-1]
        for i in range (m, 0, -1):
            dp[i][n] = dp[i+1][n] + grid[i-1][n-1]

        for i in range(m-1, 0, -1):
            for j in range(n-1, 0, -1):
                dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + grid[i-1][j-1]
        
        return dp[1][1]