class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return
            # Choice 1: include candidates[i]
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()
            # Choice 2: skip candidates[i]
            while (
                i + 1 < len(candidates)
                and candidates[i] == candidates[i + 1]
            ):
                i += 1
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res