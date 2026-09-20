from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Reverse the list so the last digit comes first.
        #
        # Example:
        # [1, 2, 9] becomes [9, 2, 1]
        #
        # This lets us process the number from right to left
        # using indices 0, 1, 2, ...
        digits = digits[::-1]

        # one represents the 1 that still needs to be added.
        #
        # one = 1 means:
        # "We still need to add one or carry one."
        #
        # one = 0 means:
        # "The addition is finished."
        one = 1

        # i is the index of the current digit.
        i = 0

        # Continue while there is still a 1 to add.
        while one:
            # Check whether i is still inside the list.
            if i < len(digits):

                # If the current digit is 9:
                #
                # 9 + 1 = 10
                #
                # Write 0 in this position and carry 1
                # to the next digit.
                if digits[i] == 9:
                    digits[i] = 0

                    # We do not set one = 0 because the carry
                    # still needs to be added to the next digit.

                else:
                    # If the digit is smaller than 9,
                    # simply add 1.
                    digits[i] += 1

                    # No carry remains, so the work is finished.
                    one = 0

            else:
                # If i is outside the list, every original digit
                # must have been 9.
                #
                # Example:
                # [9, 9] + 1 = [1, 0, 0]
                #
                # After processing the two 9s, the reversed list
                # is [0, 0], so append the remaining carry 1.
                digits.append(1)

                # The carry has now been handled.
                one = 0

            # Move to the next digit.
            i += 1

        # Reverse the digits again to restore normal order.
        return digits[::-1]