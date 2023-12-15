class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        attempts = 0
        while dp[attempts][K] < N:
            attempts += 1
            for eggs in range(1, K + 1):
                dp[attempts][eggs] = 1 + dp[attempts - 1][eggs - 1] + dp[attempts - 1][eggs]

        return attempts
