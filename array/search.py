class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1
        while left <= right: #当left和right相等时一定是解则不需要等号，如果不一定是解则需要再判断这种情况
            middle = left + (right -left)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] > nums[right]:
                if nums[left] <= target and target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] < target and target  <= nums[right]:
                    left = middle + 1
                else:
                    right = middle -1
        return -1