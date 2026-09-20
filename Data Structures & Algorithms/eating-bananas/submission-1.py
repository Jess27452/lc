import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        l = 1                  # slowest possible speed
        r = max(piles)         # fastest possible speed
        res = r               # current best answer
        while l <= r:
            k = (l + r) // 2  # try this eating speed
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                # k works
                res = min(res, k)
                r = k - 1     # try a smaller speed
            else:
                # k is too slow
                l = k + 1     # need a bigger speed
        return res