#这道题被放在了dp的类别中，但是试了一下非dp方法也能ac
#给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#子数组 是数组中的一个连续部分。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        left = 0
        right = 0
        max_num = -100000
        max_left = -1
        max_right = -1
        temp_sum = 0
        while right < len(nums):
            temp_sum = temp_sum + nums[right]
            if temp_sum > max_num:
                max_num = temp_sum
                max_left = left
                max_right = right
            if temp_sum <= 0:
                left = right + 1
                right = left
                temp_sum = 0
            else:
                right += 1
        return max_num
