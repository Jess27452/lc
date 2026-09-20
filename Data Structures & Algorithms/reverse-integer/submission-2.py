import math


class Solution:
    def reverse(self, x: int) -> int:
        # Valid signed 32-bit integer range:
        MIN = -2147483648   # -2^31
        MAX = 2147483647    # 2^31 - 1

        # res stores the reversed number being built.
        res = 0

        while x != 0:
            # Get the last digit of x.
            #
            # Examples:
            # x = 123  -> digit = 3
            # x = -123 -> digit = -3
            #
            # math.fmod is used because Python's % behaves
            # differently for negative numbers.
            digit = int(math.fmod(x, 10))

            # Remove the last digit from x.
            #
            # Examples:
            # int(123 / 10)  = 12
            # int(-123 / 10) = -12
            x = int(x / 10)

            # Before doing:
            # res = res * 10 + digit
            ## Check res and digit separately because res * 10 may still be within MAX, but adding digit can cause overflow.
            # check whether the result would exceed MAX.
            if (
                res > MAX // 10
                or (res == MAX // 10 and digit > MAX % 10)
            ):
                return 0

            # Check whether the result would go below MIN.
            #
            # We use -8 directly because the final digit of
            # the minimum integer -2147483648 is -8.
            if (
                res <= MIN//10
                or (res == int(MIN / 10) and digit < -8)
            ):
                return 0

            # Move existing digits left and append the new digit.
            #
            # Example:
            # res = 43, digit = 2
            # res = 43 * 10 + 2 = 432
            res = res * 10 + digit

        return res