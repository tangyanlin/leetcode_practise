class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                # 超过长度（第一个字符串可能比后面的长） 或 不等（不是公共字符）
                if i == len(strs[j]) or strs[j][i] != strs[0][i]: return strs[0][:i]
        return strs[0]
