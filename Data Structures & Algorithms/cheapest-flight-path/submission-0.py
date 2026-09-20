from typing import List


class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        # prices[city] stores the cheapest known price
        # from src to that city.
        prices = [float("inf")] * n

        # It costs 0 to begin at the starting city.
        prices[src] = 0

        # k stops means at most k + 1 flights.
        for i in range(k + 1):

            # Copy prices so this round only uses results
            # from the previous round.
            tempPrices = prices.copy()

            # Examine every flight.
            for source, destination, price in flights:

                # If source cannot currently be reached,
                # this flight cannot be used yet.
                if prices[source] == float("inf"):
                    continue

                # New cost if we take this flight.
                newPrice = prices[source] + price

                # Keep the cheaper price to destination.
                if newPrice < tempPrices[destination]:
                    tempPrices[destination] = newPrice

            # Save this round's answers.
            prices = tempPrices

        # If destination was never reached, return -1.
        if prices[dst] == float("inf"):
            return -1

        return prices[dst]