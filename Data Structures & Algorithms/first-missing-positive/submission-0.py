from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1:
        # Negative numbers are not useful because we only care
        # about positive integers from 1 through n.
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0

        # Step 2:
        # Use each index to record whether a number exists.
        #
        # Number 1 is represented by index 0.
        # Number 2 is represented by index 1.
        # Number 3 is represented by index 2.
        # ...
        # Number n is represented by index n - 1.
        for i in range(n):
            value = abs(nums[i])

            # Only values between 1 and n matter.
            if 1 <= value <= n:
                index = value - 1

                # A negative value means that "value" exists.
                if nums[index] > 0:
                    nums[index] *= -1

                # We cannot make 0 negative because -0 is still 0.
                # Therefore, use -(n + 1) as a negative marker.
                elif nums[index] == 0:
                    nums[index] = -(n + 1)

        # Step 3:
        # The first nonnegative position represents
        # the first missing positive integer.
        for i in range(n):
            if nums[i] >= 0:
                return i + 1

        # If every number from 1 through n exists,
        # the answer must be n + 1.
        return n + 1