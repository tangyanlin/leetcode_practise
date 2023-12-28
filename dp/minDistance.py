class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = []
        for i in range(len(word1)+1):
            temp = []
            for j in range(len(word2)+1):
                temp.append(0)
            dp.append(temp)
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] +1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        max_len = dp[len(word1)][len(word2)]
        return len(word1) -max_len + len(word2) -max_len

print(Solution().minDistance("sea", "eat"))