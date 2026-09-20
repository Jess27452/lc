from typing import List


class Solution:
    def merge(
        self,
        nums1: List[int],
        m: int,
        nums2: List[int],
        n: int
    ) -> None:
        # Index of the last available position in nums1.
        last = m + n - 1

        # Compare the largest remaining values.
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1

            last -= 1

        # If nums2 still has values, copy them into nums1.
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
        #If values from nums1 remain after nums2 is exhausted, they are already in their correct positions.