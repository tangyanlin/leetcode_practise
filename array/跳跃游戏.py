class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        max_idx = 0  # 当走到idx=i这个位置时 （0~i-1）位置元素最远能跳到的位置
        for i in range(len(nums)):
            # 走到idx=i位置了 但是max_idx<i 说明 （0~i-1）位置元素都不能到达idx=i位置
            # 也就无法往下走了
            # 注意这里是先if判断 再调整max 
            # 因为就是要在刚进入idx=i的适合 马上就判断（0~i-1）的位置能不能走到idx=i的位置   
            if max_idx < i: return False
            max_idx = max(max_idx, i + nums[i])  # 更新（0~i）位置元素最远能跳到的位置
        return True

