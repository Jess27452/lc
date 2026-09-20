class Solution:
    def canPartitionKSubsets(self, nums, k):

        # Total must be divisible by k
        if sum(nums) % k:
            return False

        nums.sort(reverse=True)

        target = sum(nums) // k

        used = [False] * len(nums)

        def backtrack(i, k, subsetSum):

            # We successfully made all k subsets
            if k == 0:
                return True

            # Current subset is complete
            if subsetSum == target:
                return backtrack(0, k - 1, 0)

            # Try adding another number to current subset
            for j in range(i, len(nums)):

                # Can't reuse number
                # Can't make subset bigger than target
                if used[j] or subsetSum + nums[j] > target:
                    continue

                # CHOOSE nums[j]
                used[j] = True

                # EXPLORE
                if backtrack(
                    j + 1,
                    k,
                    subsetSum + nums[j]
                ):
                    return True

                # UNDO / BACKTRACK
                used[j] = False

            return False

        return backtrack(0, k, 0)  