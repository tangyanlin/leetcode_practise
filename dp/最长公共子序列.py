#给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
#
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = []
        for i in range(len(text1)+1):
            temp = []
            for j in range(len(text2)+1):
                temp.append(0)
            dp.append(temp)
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] +1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len(text1)][len(text2)]
