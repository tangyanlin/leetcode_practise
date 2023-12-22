class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 1:
            return [-1, -1]
        left = 0
        right = len(nums) -1

        while left < right:
            middle = left + (right -left) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        res_left = left if nums[left] == target else -1

        left = 0
        right = len(nums) -1
        while left < right:
            middle = left + (right -left+1) // 2
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle
        res_right = left if nums[left] == target else -1

        return [res_left, res_right]
