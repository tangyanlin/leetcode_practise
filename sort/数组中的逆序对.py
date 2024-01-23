class Solution:
    def reversePairs(self, record: List[int]) -> int:
        if len(record) <= 1:
            return 0

        
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            left = 0
            right = len(nums)
            mid = (left+right)//2
            left_nums = merge_sort(nums[:mid])
            right_nums = merge_sort(nums[mid:right])
            return merge(left_nums, right_nums)

        def merge(left_nums, right_nums):
            m = len(left_nums)
            n = len(right_nums)
            result = [0]* (m+n)
            while m and n:
                if left_nums[m-1] > right_nums[n-1]:
                    self.count += n
                    result[m+n-1] = left_nums[m-1]
                    m -= 1
                else:
                    result[m+n-1] = right_nums[n-1]
                    n -= 1
            if m:
                result[:m] = left_nums[:m]
            if n:
                result[:n] = right_nums[:n]
            return result

        self.count = 0
        merge_sort(record)
        return self.count