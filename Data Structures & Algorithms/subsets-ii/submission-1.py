class Solution:
    def subsetsWithDup(self, nums):
        res = []

        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return

            # Include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # Don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtrack(i + 1, subset)

        backtrack(0, [])

        return res