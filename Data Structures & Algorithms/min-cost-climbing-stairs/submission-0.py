from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Add 0 to represent the "top" after the last stair.
        # Reaching the top itself costs 0.
        #
        # Example:
        # cost = [10, 15, 20]
        # After append:
        # cost = [10, 15, 20, 0]
        cost.append(0)

        # We start from the third-to-last index and move backwards.
        #
        # Why len(cost) - 3?
        # Because the last index is the top, cost = 0.
        # The last two real stairs can directly jump to the top,
        # so we start calculating from the stair before them.
        for i in range(len(cost) - 3, -1, -1):

            # At stair i, you must pay cost[i].
            #
            # Then you can jump either:
            # 1 step to i + 1
            # or
            # 2 steps to i + 2
            #
            # We choose the cheaper future path.
            cost[i] += min(cost[i + 1], cost[i + 2])#cost[i] = minimum total cost if you start from stair i

        # You are allowed to start from step 0 or step 1.
        # So the answer is the cheaper of those two starting choices.
        return min(cost[0], cost[1])