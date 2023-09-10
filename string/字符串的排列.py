# 题目
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

# 换句话说，s1 的排列之一是 s2 的 子串 。


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = 0
        valid = 0
        window = defaultdict(int)
        need = defaultdict(int)
        for c in s1:
            need[c] += 1
        
        while right < len(s2):
            c = s2[right]
            right = right + 1
            
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid = valid + 1
                
            while right - left >= len(s1):
                if valid == len(need):
                    return True
                d = s2[left]
                left = left +1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False
