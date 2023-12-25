class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) < 1:
            return 0
        if len(obstacleGrid[0]) < 1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1, n+1):
            if obstacleGrid[0][i-1] == 1:
                break
            dp[1][i] = 1

        for i in range(1, m+1):
            if obstacleGrid[i-1][0] == 1:
                break
            dp[i][1] = 1

        
        for i in range(2, m+1):
            for j in range(2, n+1):
                if obstacleGrid[i-1][j-1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[m][n]