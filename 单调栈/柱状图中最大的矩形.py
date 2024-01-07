class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0] 
        stack = []
        max_res = 0
        for i in range(len(heights)):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] -1
                max_res = max(max_res, height*width)
            stack.append(i)
        return max_res