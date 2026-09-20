#Notice it is still i, not i + 1.

#Because we are allowed to use the same number again.

#Full code:

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
#1. Make a choice
#2. Explore recursively
#3. Undo that exact choice
        def dfs(i, cur, total):
            # found a valid combination
            if total == target:
                res.append(cur.copy())
                return

            # invalid path
            if i >= len(candidates) or total > target:
                return

            # Choice 1: use candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
#i always means:

#which number are we currently deciding about?
            # undo the choice
            cur.pop()

            # Choice 2: skip candidates[i]
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res