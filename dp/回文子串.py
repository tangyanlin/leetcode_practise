class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) < 1:
            return 0
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        res = 0
        for i in range(len(s)):
            dp[i][i] = 1
            res += 1
        
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1: 
                        dp[i][j]=1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = 0
                res += dp[i][j]
        return res