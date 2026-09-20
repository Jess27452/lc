from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left = buying day
        # right = selling day
        left = 0
        right = 1

        max_profit = 0

        while right < len(prices):

            # Selling price is higher than buying price.
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)

            else:
                # We found a cheaper buying price.
                left = right

            # Try the next selling day.
            right += 1

        return max_profit