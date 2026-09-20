class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []

        def dfs(i):

            # reached end of array
            if i >= len(nums):
                res.append(subset.copy())
                return

            # include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # NOT include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res