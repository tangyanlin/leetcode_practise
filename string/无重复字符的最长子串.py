#
#给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        length = 0
        window = defaultdict(int)
        flag = True
        while right < len(s):
            c = s[right]
            right = right + 1
            window[c] += 1
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            length = max(length, right -left)
        
        return length
