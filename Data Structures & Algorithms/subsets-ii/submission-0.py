class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        def backtrack(i, subset):
            # reached the end
            if i == len(nums):
                res.append(subset.copy())
                return

            # Choice 1: include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # undo include choice
            subset.pop()

            # Choice 2: skip nums[i]
            # skip all duplicates of nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtrack(i + 1, subset)

        backtrack(0, [])
        return res

        #1. include
#2. recurse
#3. pop (backtrack)
#4. skip duplicates
#5. recurse