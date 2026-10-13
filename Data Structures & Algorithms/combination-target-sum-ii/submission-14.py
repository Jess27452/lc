
        #eg[1,1,2]
        #We skip the second 1 because we already explored all combinations starting with the first 1.
class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        cur = []

        def dfs(start, total):
            if total == target:
                res.append(cur.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Choose
                cur.append(candidates[i])

                # Explore
                dfs(i + 1, total + candidates[i])

                # Backtrack
                cur.pop()

        dfs(0, 0)
        return res