from typing import List


class Solution:
    def minSubArrayLen(
        self,
        target: int,
        nums: List[int]
    ) -> int:
        left = 0
        total = 0

        # Start with infinity because we have not found
        # a valid subarray yet.
        result = float("inf")

        for right in range(len(nums)):
            # Add the new right-side number to the window.
            total += nums[right]

            # As long as the sum is large enough,
            # record the length and keep shrinking.
            while total >= target:
                current_length = right - left + 1
                result = min(result, current_length)

                # Remove the leftmost number.
                total -= nums[left]

                # Move the left boundary right.
                left += 1

        # If result is still infinity, no valid subarray existed.
        return 0 if result == float("inf") else result