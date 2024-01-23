class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        max_len = 0
        for num in res:
            if num -1 not in res:
                cur_start = num
                i = 1
                while cur_start+1 in res:
                    cur_start += 1
                    i += 1
                max_len = max(max_len, i)
        return max_len