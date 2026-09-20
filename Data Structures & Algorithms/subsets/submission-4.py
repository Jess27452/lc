class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, subset):
            # We've considered every number
            if i == len(nums):
                res.append(subset.copy())
                return

            # Choice 1: include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # Undo the choice
            subset.pop()

            # Choice 2: don't include nums[i]
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res

        