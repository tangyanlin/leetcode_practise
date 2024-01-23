class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(len(s)+1):
            for j in range(i, 0, -1):
                if s[j-1:i] in wordDict:
                    print(i,j)
                    print(s[j-1:i-1])
                    dp[i] = dp[i] or dp[j-1]
                    print(dp[i])
        return dp[len(s)]