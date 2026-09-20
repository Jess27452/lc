class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        # Stores the largest valid number found so far.
        result = 0

        while left <= right:
            middle = left + (right - left) // 2

            if middle * middle > x:
                # middle is too large.
                right = middle - 1

            elif middle * middle < x:
                # middle could be the answer,
                # but there might be a larger valid number.
                result = middle
                left = middle + 1

            else:
                # middle * middle == x
                return middle

        return result