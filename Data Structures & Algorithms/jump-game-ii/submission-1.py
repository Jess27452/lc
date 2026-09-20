class Solution:
    def jump(self, nums: List[int]) -> int:
        # res = number of jumps we have made so far
        res = 0

        # l and r represent the current range of indices
        # we can reach using the current number of jumps
        #
        # At the beginning:
        # we have made 0 jumps, so we can only be at index 0
        l = r = 0

        # Keep going until our reachable range includes
        # the last index
        while r < len(nums) - 1:

            # farthest = farthest index we can reach
            # after making ONE more jump
            farthest = 0

            # Check every index in our current reachable range
            for i in range(l, r + 1):

                # From index i, the farthest we can jump is:
                # i + nums[i]
                #
                # Keep the maximum among all positions
                # in the current range
                farthest = max(farthest, i + nums[i])

            # Our next reachable range starts
            # right after the old range
            l = r + 1

            # And ends at the farthest index
            # we found above
            r = farthest

            # Moving to this new range means
            # we used one more jump
            res += 1

        # Minimum number of jumps needed
        return res