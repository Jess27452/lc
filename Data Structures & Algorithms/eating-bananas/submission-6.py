import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Possible eating speeds:
        # minimum = 1 banana/hour
        # maximum = the largest pile
        left = 1
        right = max(piles)

        # Start with a speed that is definitely fast enough.
        result = right

        while left <= right:
            # Try the middle eating speed.
            speed = left + (right - left) // 2

            # Calculate how many hours this speed requires.
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / speed)

            if hours <= h:
                # This speed works.
                result = min(result, speed)

                # But we want the MINIMUM working speed,
                # so search for a smaller speed.
                right = speed - 1

            else:
                # This speed is too slow.
                # Search for a faster speed.
                left = speed + 1

        return result