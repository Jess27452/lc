class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return

            # Choice 1: USE candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # Undo the choice
            cur.pop()

            # Choice 2: SKIP candidates[i]
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res