from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:

        def reverse(left: int, right: int) -> None:
            # Continue while the two pointers have not met.
            if left < right:
                # Swap the characters at the two ends.
                s[left], s[right] = s[right], s[left]
#temp = s[left]
#s[left] = s[right]
#s[right] = temp
                # Move both pointers toward the center.
                reverse(left + 1, right - 1)

        reverse(0, len(s) - 1)
        