from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        output = []          # Stores the maximum for each window

        q = deque()          # Stores indexes of potential maximums
                             # Values corresponding to these indexes
                             # are kept in decreasing order

        l = r = 0            # Left and right pointers of sliding window

        while r < len(nums): # Move right pointer through array

            # Remove smaller values from the back of deque
            # because the current value is bigger and newer,
            # so those smaller values can never be maximum again
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # Add current index into deque
            q.append(r)

            # Remove the front index if it is outside
            # the current window
            if l > q[0]:
                q.popleft()

            # Window is fully formed when size reaches k
            if (r + 1) >= k:

                # Front of deque is always the maximum
                output.append(nums[q[0]])

                # Slide window by moving left pointer
                l += 1

            # Expand window by moving right pointer
            r += 1

        return output