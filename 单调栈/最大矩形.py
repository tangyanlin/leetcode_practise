class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        def get_heights(arr, heights):  
            # 根据上一层的heights求当前层的heights
            for i in range(len(arr)):
                if arr[i] == '0':
                    heights[i] = 0
                else:
                    heights[i] += 1
            return heights
        def largestRectangleArea(heights):
            # 求柱状图中最大的矩形 和84一模一样
            stack = []  # 单调递增栈
            maxArea = 0
            heights = [0] + heights + [0]
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    maxArea = max(maxArea, h*w)
                stack.append(i)
            return maxArea
        # 把二维矩形才成一个个的一位矩形 判断最大面积
        max_area = 0
        for i in range(len(matrix)):
            if i == 0:
                heights = list(map(int, matrix[i]))
            else:
                heights = get_heights(matrix[i], heights)
            
            cur_row_max_area = largestRectangleArea(heights)
            max_area = max(max_area, cur_row_max_area)
        return max_area
