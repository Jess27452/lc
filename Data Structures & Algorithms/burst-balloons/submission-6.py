from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add virtual balloons with value 1 to both ends.
        #
        # Example:
        # Original: [3, 1, 5, 8]
        # New:      [1, 3, 1, 5, 8, 1]
        #
        # This avoids special cases for the first and last balloons.
        nums = [1] + nums + [1]

        # dp[(l, r)] stores the maximum coins obtainable
        # by bursting all balloons from index l to index r.
        dp = {}

        def dfs(l: int, r: int) -> int:
            # Base case:
            # If l > r, the interval contains no balloons.
            # Therefore, we gain 0 coins.
            if l > r:
                return 0

            # If we have already solved this interval,
            # return the saved answer instead of repeating the work.
            if (l, r) in dp:
                return dp[(l, r)]

            # Start with 0 coins for this interval.
            dp[(l, r)] = 0

            # Try every balloon i as the LAST balloon
            # to be burst inside the interval [l, r].
            for i in range(l, r + 1):

                # Because i is burst last, all other balloons
                # inside [l, r] have already disappeared.
                #
                # Therefore, the balloons next to nums[i] are:
                # nums[l - 1] on the left
                # nums[r + 1] on the right
                coins_from_bursting_i_last = (
                    nums[l - 1] * nums[i] * nums[r + 1]
                )

                # Before bursting i last, we must burst:
                #
                # 1. Every balloon to the left of i:
                #    interval [l, i - 1]
                #
                # 2. Every balloon to the right of i:
                #    interval [i + 1, r]
                left_coins = dfs(l, i - 1)
                right_coins = dfs(i + 1, r)

                # Total coins when i is chosen as the last balloon.
                total_coins = (
                    left_coins
                    + coins_from_bursting_i_last
                    + right_coins
                )

                # Compare this choice with previous choices.
                # Keep the maximum result.
                dp[(l, r)] = max(dp[(l, r)], total_coins)

            # Return the best answer for interval [l, r].
            return dp[(l, r)]

        # The real balloons start at index 1 because index 0
        # contains the added boundary balloon.
        #
        # The real balloons end at len(nums) - 2 because the final
        # index contains the other added boundary balloon.
        return dfs(1, len(nums) - 2)