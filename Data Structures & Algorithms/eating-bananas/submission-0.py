class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def can_finish(k: int) -> bool:
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k   # ceil(p/k)
                if hours > h:               # early stop if already too many hours
                    return False
            return True

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid      # mid works, try smaller k
            else:
                left = mid + 1   # mid too slow, need bigger k

        return left