class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #eg:[1,1,6]
        #we tried using 6
#then we tried skipping 6
#there are no more numbers
#so this path ends

        res = []
        # sort so duplicate numbers are next to each other
        candidates.sort()

        def dfs(i, cur, total):
            # found one valid combination
            if total == target:
                res.append(cur.copy())
                return

            # invalid path
            if total > target or i == len(candidates):
                return

            # Choice 1: include candidates[i]
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])

            # undo include choice
            cur.pop()

            # Choice 2: skip candidates[i]
            # skip all duplicate values#The reason for skipping:is to avoid duplicate answers.
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res