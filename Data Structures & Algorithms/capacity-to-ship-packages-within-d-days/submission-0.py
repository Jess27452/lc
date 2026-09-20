from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Smallest possible capacity:
        # the ship must carry the heaviest single package.
        left = max(weights)

        # Largest necessary capacity:
        # carry every package in one day.
        right = sum(weights)

        result = right

        def can_ship(capacity: int) -> bool:
            # Start on day 1.
            days_used = 1

            # Remaining capacity for the current day.
            remaining_capacity = capacity

            for weight in weights:
                # The current package does not fit today.
                if remaining_capacity - weight < 0:
                    # Start a new shipping day.
                    days_used += 1

                    # Reset the new day's available capacity.
                    remaining_capacity = capacity

                # Load the current package.
                remaining_capacity -= weight

            # This capacity works if we finish within the limit.
            return days_used <= days

        while left <= right:
            capacity = left + (right - left) // 2

            if can_ship(capacity):
                # This capacity works, so save it.
                result = min(result, capacity)

                # Search for a smaller working capacity.
                right = capacity - 1
            else:
                # This capacity is too small.
                left = capacity + 1

        return result