from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Number of subarrays whose sum equals k.
        result = 0

        # Running prefix sum from nums[0] to the current position.
        current_sum = 0

        # prefix_sums[sum_value] = how many times this prefix sum
        # has appeared so far.
        #
        # A prefix sum of 0 exists once before we process any numbers.
        prefix_sums = {0: 1}

        for number in nums:
            # Add the current number to the running sum.
            current_sum += number

            # We need an earlier prefix sum equal to:
            # current_sum - previous_sum = k
            #
            # Therefore:
            # previous_sum = current_sum - k
            needed_sum = current_sum - k

            # Every occurrence of needed_sum creates one valid subarray
            # ending at the current position.
            result += prefix_sums.get(needed_sum, 0)

            # Save the current prefix sum for future positions.
            prefix_sums[current_sum] = (
                prefix_sums.get(current_sum, 0) + 1
            )

        return result