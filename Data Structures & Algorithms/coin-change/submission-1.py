class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[a] = minimum number of coins needed to make amount a
        dp = [amount + 1] * (amount + 1)

        # base case
        dp[0] = 0

        # build dp from 1 to amount
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:###Try every coin as the LAST move
                    dp[a] = min(dp[a], 1 + dp[a - c])
#######dp[a] = best among:
  #  (take coin c last + solve rest)
        # if still impossible, return -1
        return dp[amount] if dp[amount] != amount + 1 else -1