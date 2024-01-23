class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums: return ""
        def quick_sort(nums, left, right):
            if left >= right: return 
            temp, i, j = left, left, right
            while i < j:
                # 从大到小排列(比的是第一个数字的大小)
                # 右边碰到比它小  j-=1
                while i < j and (nums[j]+nums[temp]) < (nums[temp]+nums[j]):
                    j -= 1
                # 左边碰到比它大  i+=1
                while i < j and (nums[i]+nums[temp]) >= (nums[temp]+nums[i]):
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[temp], nums[i] = nums[i], nums[temp]
            quick_sort(nums, left, j-1)
            quick_sort(nums, j+1, right)
        nums = list(map(str, nums))   # [10,2] -> ['10', '2']
        quick_sort(nums, 0, len(nums)-1)
        non_zero_loc = 0
        while non_zero_loc < len(nums)-1 and nums[non_zero_loc] == '0':
            non_zero_loc += 1
        return ''.join(nums[non_zero_loc:])  # ["10","2"] -> "102"
