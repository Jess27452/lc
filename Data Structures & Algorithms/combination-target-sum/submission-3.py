class Solution:
    def combinationSum(self, nums, target):
        res = []

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i == len(nums) or total > target:
                return

            # Take nums[i]
            cur.append(nums[i])
            backtrack(i, cur, total + nums[i])

            # Don't take nums[i]
            cur.pop()
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)

        return res
