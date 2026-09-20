from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)

        # Before using any numbers, there is exactly one way
        # to have a sum of 0: choose nothing.
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)

            for current_sum, count in dp.items():
                # Put a plus sign before num.
                next_dp[current_sum + num] += count

                # Put a minus sign before num.
                next_dp[current_sum - num] += count

            dp = next_dp
#So after processing k numbers:

#dp contains only expressions that used exactly those k numbers.

#After the entire outer loop finishes:

#dp contains only expressions that used every number in nums.
        return dp[target]