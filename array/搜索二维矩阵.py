class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = m-1
        right = 0

        while right < n and left >= 0:
            if matrix[left][right] < target:
                right += 1
            elif matrix[left][right] > target:
                left -= 1
            else:
                return True
        return False
