# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# The guess API is already provided by LeetCode.
# You do not need to write it yourself.
#
# guess(num) returns:
# -1 if the hidden number is lower than num
#  1 if the hidden number is higher than num
#  0 if num is correct


class Solution:
    def guessNumber(self, n: int) -> int:
        # The hidden number must be between 1 and n.
        left = 1
        right = n

        while left <= right:
            # Find the middle number of the current range.
            middle = left + (right - left) // 2

            # Ask whether middle is too low, too high, or correct.
            result = guess(middle)

            if result == 1:
                # The hidden number is higher than middle.
                # Search the right side.
                left = middle + 1

            elif result == -1:
                # The hidden number is lower than middle.
                # Search the left side.
                right = middle - 1

            else:
                # result == 0, so middle is the hidden number.
                return middle

        # The problem guarantees that a valid hidden number exists.
        return -1