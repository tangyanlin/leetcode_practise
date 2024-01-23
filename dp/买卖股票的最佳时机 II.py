class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 可以完成多次交易，但是同一时刻只能持有一只股
        if len(prices) < 2: return 0
        # dp[i][0]表示第i天未持股状态下所获最大利润
        # dp[i][1]表示第i天持股状态下所获最大利润
        dp = [[0 for _ in range(2)]for _ in range(len(prices))]
        dp[0][0], dp[0][1] = 0, -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            # 因为可以买卖多次，所以昨天没持股的情况下是可能会有利润的 
            # 所以用dp[i-1][0]-prices[i]得到昨天没持股，今天持股的最大利润
            dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
        # 第i天不持股最大利润肯定大于持股最大利润
        return dp[-1][0]
