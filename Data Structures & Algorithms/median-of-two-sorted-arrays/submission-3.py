from typing import List


class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> float:

        # Give shorter names to the arrays.
        A = nums1
        B = nums2

        # Total number of elements in both arrays.
        total = len(A) + len(B)

        # Number of elements needed on the left side.
        half = total // 2

        # Always binary-search the smaller array.
        if len(A) > len(B):
            A, B = B, A

        # Binary-search indexes in A.
        left = 0
        right = len(A) - 1

        while True:
            # i is the index of the last A element
            # placed on the left side.
            i = left + (right - left) // 2

            # j is the index of the last B element
            # placed on the left side.
            j = half - i - 2

            # Values around A's partition.
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")

            # Values around B's partition.
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            # Correct partition:
            # every left-side value is <= every right-side value.
            if Aleft <= Bright and Bleft <= Aright:

                # Odd total: median is the smallest value
                # on the right side.
                if total % 2 == 1:
                    return min(Aright, Bright)

                # Even total: average the largest left value
                # and the smallest right value.
                return (
                    max(Aleft, Bleft)
                    + min(Aright, Bright)
                ) / 2

            # Aleft is too large, so move A's partition left.
            elif Aleft > Bright:
                right = i - 1

            # Bleft is too large compared with Aright,
            # so move A's partition right.
            else:
                left = i + 1