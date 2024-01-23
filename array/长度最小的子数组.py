class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        start, win_sum, wim_len = 0, 0, 0
        for end in range(len(nums)):
            # end往后移
            win_sum += nums[end]
            # start往前移 知道不满足条件
            while win_sum >= target:
                win_len = end - start + 1
                min_len = min(min_len, win_len)
                win_sum -= nums[start]
                start += 1
        return 0 if min_len == float('inf') else min_len
