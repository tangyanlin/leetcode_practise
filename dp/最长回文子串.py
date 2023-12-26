class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return 0
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        max_res = 1
        left = 0
        right = 0
        for i in range(len(s)):
            dp[i][i] = 1
            
        
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1: 
                        dp[i][j]=1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] == 1 and max_res < j-i+1:
                    max_res = j-i+1
                    left = i
                    right = j
        return s[left:right+1]