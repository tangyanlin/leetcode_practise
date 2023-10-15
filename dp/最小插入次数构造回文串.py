
class Solution:
    def minInsertions(self, s: str) -> int:
        dp = []
        for i in range(len(s)):
            temp = []
            for j in range(len(s)):
                temp.append(0)
            dp.append(temp)
        
        
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j] + 1, dp[i][j-1] +1)
        
        return dp[0][len(s)-1]
