class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A #Always make A the smaller array.#Always make B the bigger array.


        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2#left side of A+left side of B=half#(i+1) + (j+1) = half#i + j + 2 = half#j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")# with infinity the normal comparison still works: Aleft <= Bright
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:# means if total is odd
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:#We took too many elements from A.
                r = i - 1
            else:#We didn't take enough elements from A.Need more elements from A on the left.
                l = i + 1