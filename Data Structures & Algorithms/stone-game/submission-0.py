from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        # returns the maximum total Alice can get
        # from piles[l:r+1]
        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in dp:
                return dp[(l, r)]

            # True when it is Alice's turn
            even = True if (r - l) % 2 else False

            # Alice gets points on her turn.
            # On Bob's turn, Alice gets 0 points.
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            dp[(l, r)] = max(
                dfs(l + 1, r) + left,   # take left pile
                dfs(l, r - 1) + right   # take right pile
            )

            return dp[(l, r)]

        return dfs(0, len(piles) - 1) > sum(piles) // 2