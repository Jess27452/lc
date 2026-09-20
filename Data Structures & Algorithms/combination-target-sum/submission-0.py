from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # res will store ALL valid combinations we find.
        # Example final answer could be:
        # [[2, 2, 3], [7]]
        res = []

        def dfs(i: int, cur: List[int], total: int) -> None:#dfs updates res not rteurning thinsg
            """
            i     = the current index we are considering in candidates
            cur   = the current combination we are building
            total = the sum of the numbers currently inside cur

            Example:
            if candidates = [2, 3, 6, 7]
            and we are at dfs(1, [2, 2], 4),
            that means:
              - we are currently looking at candidates[1], which is 3
              - our current combination is [2, 2]
              - its sum is 4
            """

            # --------------------------------------------------
            # BASE CASE 1: We found a valid combination
            # --------------------------------------------------
            if total == target:
                # We MUST append cur.copy(), NOT cur
                #
                # Why?
                # Because cur is the SAME list object used during recursion.
                # Later, backtracking will do cur.pop(), which changes cur.
                #
                # If we did:
                #     res.append(cur)
                # then res would store a reference to the SAME list,
                # and later backtracking would accidentally change the
                # saved answer inside res.
                #
                # Example:
                #   cur = [2, 3]
                #   res.append(cur)        # WRONG
                #   cur.pop()             # backtracking
                #   now cur = [2]
                #   and res becomes [[2]] instead of [[2,3]]
                #
                # But with cur.copy():
                #   cur = [2, 3]
                #   res.append(cur.copy())  # stores a SEPARATE list
                #   cur.pop()
                #   cur becomes [2]
                #   res stays [[2,3]]
                res.append(cur.copy())
                return

            # --------------------------------------------------
            # BASE CASE 2: Stop if path is invalid
            # --------------------------------------------------
            if i >= len(candidates) or total > target:
                # Stop if:
                # 1. i is out of bounds -> no more numbers left
                # 2. total is already too big -> cannot recover
                return

            # ==================================================
            # CHOICE 1: TAKE candidates[i]
            # ==================================================

            # Add the current candidate into the current path.
            #
            # Example:
            #   cur = [2, 2]
            #   candidates[i] = 3
            # after append:
            #   cur = [2, 2, 3]
            cur.append(candidates[i])

            # Recurse using the SAME index i.
            #
            # Why same i?
            # Because the problem says we may reuse the same number
            # unlimited times.
            #
            # So if candidates[i] is 2, we can do:
            # [2], [2,2], [2,2,2], ...
            dfs(i, cur, total + candidates[i])

            # --------------------------------------------------
            # BACKTRACKING HAPPENS HERE
            # --------------------------------------------------
            # This line UNDOES the choice we just made above.
            #
            # Pattern:
            #   choose
            #   recurse
            #   undo choice   <-- this is backtracking
            #
            # Example:
            #   cur was [2, 2, 3]
            #   cur.pop()
            #   now cur becomes [2, 2]
            #
            # Why do we do this?
            # Because after exploring the branch where we TOOK
            # candidates[i], we now want to explore the branch
            # where we SKIP candidates[i].
            #
            # Backtracking means restoring cur to the earlier state
            # before trying another path.
            cur.pop()

            # ==================================================
            # CHOICE 2: SKIP candidates[i]
            # ==================================================
            # Move to the next index.
            #
            # We do NOT change total here because we are not taking
            # candidates[i] in this branch.
            #
            # Example:
            # if currently i = 0 and candidates[0] = 2,
            # then dfs(i + 1, cur, total) means:
            # "I'm done trying 2, now move to 3."
            dfs(i + 1, cur, total)

        # Start recursion from:
        # i = 0       -> first candidate
        # cur = []    -> empty current combination
        # total = 0   -> current sum is 0
        dfs(0, [], 0)

        return res