from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the final digit and move backward.
        for i in range(len(digits) - 1, -1, -1):
            # If the digit is smaller than 9,
            # add one and immediately return.
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If the digit is 9, it becomes 0,
            # and the carry continues left.
            digits[i] = 0

        # If every digit was 9, we need a new leading 1.
        #
        # Example:
        # [9, 9] becomes [0, 0] during the loop,
        # then returns [1, 0, 0].
        return [1] + digits