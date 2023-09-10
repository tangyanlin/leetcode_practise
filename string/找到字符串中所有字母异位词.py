# 题目
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        right = 0
        valid = 0
        window = defaultdict(int)
        need = defaultdict(int)
        for c in p:
            need[c] += 1
        result = []
        while right < len(s):
            c = s[right]
            right = right + 1
            
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid = valid + 1
                
            while right - left >= len(p):
                if valid == len(need):
                    result.append(left)
                d = s[left]
                left = left +1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return result
