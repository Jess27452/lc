class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []       # stores all final subsets
        subset = []    # current subset we are building

        def dfs(i):
            # if i reaches the end, we made one complete subset
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Choice 1: include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Choice 2: do NOT include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res