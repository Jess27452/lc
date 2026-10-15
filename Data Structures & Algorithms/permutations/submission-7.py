class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i):
            # all positions filled
            if i == len(nums):
                res.append(nums.copy())
                return

            # try every remaining number at position i
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]  # choose
                dfs(i + 1)                           # fill next position
                nums[i], nums[j] = nums[j], nums[i]  # undo

        dfs(0)
        return res

        #“I’ll use backtracking. At each index i, I choose which remaining number should go into that position. I swap each candidate into position i, recurse to fill the next position, then swap back to undo the choice and try another candidate. Once i == len(nums), all positions are filled, so I copy the current array into the result.”