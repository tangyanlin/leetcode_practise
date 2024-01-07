class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) == 0:
            return 0
        
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                cur = height[stack.pop()]
                if not stack: break
                h = min(height[stack[-1]], height[i]) - cur
                res += h * (i - stack[-1] - 1)
            stack.append(i)
        return res