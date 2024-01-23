class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n0, n1, n2 = 0, 0, 0
        for num in nums:
            if num == 0:
                n0+=1
            elif num == 1:
                n1+=1
            elif num == 2:
                n2 += 1
        nums[:n0] = [0] * n0
        nums[n0:n1+n0] = [1] * n1
        nums[n1+n0:] = [2]*n2