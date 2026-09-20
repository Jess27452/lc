from typing import List


class Solution:
    def findClosestElements(
        self,
        arr: List[int],
        k: int,
        x: int
    ) -> List[int]:

        # Possible starting indices of a length-k window:
        # 0 through len(arr) - k
        left = 0
        right = len(arr) - k

        while left < right:
            middle = left + (right - left) // 2

            # Compare:
            # arr[middle]     = left element of the current window
            # arr[middle + k] = the next element outside the window
            #
            # If the left element is farther from x,
            # move the window to the right.
            if x - arr[middle] > arr[middle + k] - x:
                left = middle + 1
            else:
                right = middle

        # left is the best starting index.
        return arr[left:left + k]   
#The correct answer always stays inside [left, right].

#Every iteration removes impossible positions.

#When left == right, only the correct position remains.
          