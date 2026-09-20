from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)

        D = deque()
        R = deque()

        # Store the index of every senator
        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)

        # Keep going while both parties still have senators
        while D and R:

            # Get the senator whose turn comes earliest
            dTurn = D.popleft()
            rTurn = R.popleft()

            # Whoever has the smaller index acts first
            if rTurn < dTurn:
                # R acts first → bans this D senator
                #
                # R survives and gets another turn NEXT round.
                # Add len(senate) so its new turn comes later.
                R.append(rTurn + len(senate))

            else:
                # D acts first → bans this R senator
                #
                # D survives and gets another turn next round.
                D.append(dTurn + len(senate))

        # If R queue still has senators, Radiant wins.
        # Otherwise Dire wins.
        return "Radiant" if R else "Dire"