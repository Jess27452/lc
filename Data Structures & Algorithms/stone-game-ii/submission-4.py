from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # dp[(alice, i, M)] = maximum stones Alice can get
        # from this game state
        dp = {}

        def dfs(alice, i, M):
            # No piles left
            if i == len(piles):
                return 0

            # Already solved this state
            if (alice, i, M) in dp:
                return dp[(alice, i, M)]

            # Alice maximizes; Bob minimizes Alice's score
            res = 0 if alice else float("inf")

            # Stones in the first X piles being considered
            total = 0

            # Current player can take X piles, where 1 <= X <= 2M
            for X in range(1, 2 * M + 1):

                # Cannot take more piles than remain
                if i + X > len(piles):
                    break

                # Add the next pile to the amount being taken
                total += piles[i + X - 1]

                if alice:
                    # Alice takes these stones, so add total
                    # Then switch to Bob's turn
                    res = max(
                        res,
                        total + dfs(
                            False,
                            i + X,
                            max(M, X)
                        )
                    )

                else:
                    # Bob takes the stones, so Alice gets 0 now
                    # Bob chooses the move minimizing Alice's result
                    res = min(
                        res,
                        dfs(
                            True,
                            i + X,
                            max(M, X)
                        )
                    )

            # Save best answer for this state
            dp[(alice, i, M)] = res
            return res

        # Start with Alice, first pile, M = 1
        return dfs(True, 0, 1)