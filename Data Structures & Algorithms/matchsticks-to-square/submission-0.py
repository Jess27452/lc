class Solution:
    def makesquare(self, matchsticks):

        length = sum(matchsticks) // 4

        sides = [0] * 4

        if sum(matchsticks) % 4 != 0:
            return False

        matchsticks.sort(reverse=True)

        def backtrack(i):

            # used all matchsticks
            if i == len(matchsticks):
                return True

            # try putting current stick on each side
            for j in range(4):

                if sides[j] + matchsticks[i] <= length:

                    # choose
                    sides[j] += matchsticks[i]

                    if backtrack(i + 1):
                        return True

                    # undo choice
                    sides[j] -= matchsticks[i]

            return False

        return backtrack(0)      