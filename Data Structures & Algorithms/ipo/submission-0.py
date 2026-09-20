from typing import List
import heapq


class Solution:
    def findMaximizedCapital(
        self,
        k: int,
        w: int,
        profits: List[int],
        capital: List[int]
    ) -> int:

        # Stores projects we have not yet made affordable:
        # (required_capital, profit)
        min_capital = [
            (required_capital, profit)
            for required_capital, profit in zip(capital, profits)
        ]

        # Smallest required capital appears at the top.
        heapq.heapify(min_capital)

        # Stores profits of projects we can currently afford.
        # Negative profits simulate a max-heap.
        max_profit = []

        # We may complete at most k projects.
        for _ in range(k):

            # Move every currently affordable project
            # from min_capital into max_profit.
            while min_capital and min_capital[0][0] <= w:
                required_capital, profit = heapq.heappop(min_capital)
                heapq.heappush(max_profit, -profit)

            # No affordable project is available.
            if not max_profit:
                break

            # Choose the affordable project with the largest profit.
            best_profit = -heapq.heappop(max_profit)

            # Add its profit to our current capital.
            w += best_profit# we dont need to consume capital

        return w