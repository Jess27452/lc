from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[(i, buying)] stores the maximum profit starting
        # from day i with the given buying state.
        dp = {}

        def dfs(i: int, buying: bool) -> int:
            # No more days remain.
            if i >= len(prices):
                return 0

            # Return the saved answer if this state was solved before.
            if (i, buying) in dp:
                return dp[(i, buying)]

            # Option available in both states:
            # do nothing today and move to the next day.
            cooldown = dfs(i + 1, buying)

            if buying:
                # Buy today:
                # subtract today's price and change to the selling state.
                buy = dfs(i + 1, False) - prices[i]

                dp[(i, buying)] = max(buy, cooldown)

            else:
                # Sell today:
                # add today's price.
                #
                # Move to i + 2 because the next day is the required
                # cooldown day.
                sell = dfs(i + 2, True) + prices[i]
#buying == True

#You do not currently own a coin, so you are allowed to buy.
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        # We begin on day 0 without owning a coin,
        # so we are allowed to buy.
        return dfs(0, True)