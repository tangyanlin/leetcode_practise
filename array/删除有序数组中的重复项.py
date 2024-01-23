class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        new_index = 0
        ele = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != ele:
                nums[new_index] = ele
                new_index += 1
                ele = nums[i]
        return new_index
            
