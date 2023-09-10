# 题目
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        valid = 0
        window = defaultdict(int)
        need = defaultdict(int)
        start = 0
        length = 1000000
        for c in t:
            need[c] += 1
        
        while right < len(s):
            c = s[right]
            right = right + 1
            
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid = valid + 1
                
            while valid == len(need):
                
                if right - left < length:
                    start = left
                    length = right - left
                    
                d = s[left]
                left = left + 1
                
                if d in need:
                    if window[d] == need[d]:
                        valid = valid - 1
                    window[d] = window[d] - 1
        return s[start:length+start] if length < 1000000 else ''
