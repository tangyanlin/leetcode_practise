class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 最多总共完成2次交易 同时最多只能完成一次交易
        if len(prices) < 2: return 0
        # dp[i][j][k]表示第i天 持股状态为j 交易次数为k的情况下所获的最大利润
        # i=0~(len(price)-1)  j: 0不持股 1持股   k: 0次交易 1次交易 2次交易
        dp = [[[0 for _ in range(3)]for _ in range(2)]for _ in range(len(prices))]
        dp[0][0][0] = 0
        dp[0][1][0] = -prices[0]
        dp[0][0][1] = dp[0][0][2] = dp[0][1][1] = dp[0][1][2] = float('-inf') # 不可能事件
        for i in range(1, len(prices)):
            dp[i][0][0] = 0 
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][1][0]+prices[i])
            dp[i][0][2] = max(dp[i-1][0][2], dp[i-1][1][1]+prices[i])
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][0]-prices[i])
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][1]-prices[i])
            dp[i][1][2] = float("-inf")  # 不可能事件
        # 注意最大利润可能为负
        return max(0, dp[-1][0][1], dp[-1][0][2])
