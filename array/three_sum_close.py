class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):

            j,k = i+1, len(nums)-1
            while j < k:
                r_target = nums[j] + nums[k] + nums[i]
                if abs(r_target-target) < abs(res -target):
                    res = r_target
                if nums[j] + nums[k] + nums[i] < target:
                    j += 1
                elif nums[j] + nums[k] + nums[i] > target:
                    k -= 1
                else:
                    return target
        return res