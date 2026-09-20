from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(
        self,
        nums: List[int],
        k: int
    ) -> List[int]:

        result = []

        # Stores indices, not the actual numbers.
        #
        # The values corresponding to these indices
        # are kept in decreasing order.
        q = deque()

        # Left and right boundaries of the window.
        left = 0

        for right in range(len(nums)):

            # Remove smaller values from the back.
            #
            # nums[q[-1]] is the value at the index
            # currently at the back of the deque.
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # Add the current index.
            q.append(right)

            # Remove the index at the front if it is
            # outside the current window.
            if q[0] < left:
                q.popleft()

            # The first complete window has formed when:
            #
            # right - left + 1 == k
            if right - left + 1 == k:

                # The front of the deque always stores
                # the index of the largest value.
                result.append(nums[q[0]])

                # Move the window one position right.
                left += 1

        return result    