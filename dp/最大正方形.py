from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        if len(matrix) < 1:
            return -1
        if len(matrix[0]) < 1:
            return -1
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        max_result = 0
        for i in range(m):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                max_result = max(max_result, dp[i][0])
        
        for i in range(n):
            if matrix[0][i]  == '1':
                dp[0][i] = 1
                max_result = max(max_result, dp[0][i])
        
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_result = max(max_result, dp[i][j])
        return max_result**2

print(Solution().maximalSquare([["0","1"]]))
