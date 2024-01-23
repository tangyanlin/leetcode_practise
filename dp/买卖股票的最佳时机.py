class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0 
        max_res = 0
        inp = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < inp:
                inp = prices[i]
            else:
                max_res = max(max_res, prices[i]-inp)
        return max_res
