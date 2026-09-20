from typing import List
from math import ceil

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)

        # Try to build one group whose sum is near half
        target = ceil(stoneSum / 2)

        # memo: (index, current_sum) -> best answer
        dp = {}

        def dfs(i, total):
            # If we reached/passed half, or used all stones
            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total))

            # Already solved this state
            if (i, total) in dp:
                return dp[(i, total)]

            # Choice: skip stone i OR put stone i in our group
            dp[(i, total)] = min(
                dfs(i + 1, total),              # don't take
                dfs(i + 1, total + stones[i])   # take
            )
#for dp: starting at stone index i, with current chosen sum total, what is the minimum final difference I can get?
            return dp[(i, total)]

        return dfs(0, 0)