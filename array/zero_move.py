class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        none_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[none_zero_index] = nums[i]
                none_zero_index += 1
        for i in range(none_zero_index, len(nums)):
            nums[i] = 0
                    