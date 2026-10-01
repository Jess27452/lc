class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[a] = number of combinations to make amount a
        dp = [0] * (amount + 1)

        # One way to make 0: choose no coins
        dp[0] = 1

        # Coin outside -> count combinations, not permutations
        for coin in coins:

            # Forward -> current coin can be reused unlimited times
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]

        return dp[amount]