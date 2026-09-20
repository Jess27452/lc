class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s

                if target - square < 0:
                    break

                dp[target] = min(
                    dp[target],
                    1 + dp[target - square]
                )

        return dp[n]
    #dp[target] minimum number of perfect squares to make target
    #1 + dp[target - square]

#means:

#use one square now, then add the minimum number of squares needed for the leftover amount.