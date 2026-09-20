from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # count of characters needed from t
        countT = Counter(t)
        window = {}

        # how many requirements we have satisfied
        have, need = 0, len(countT)

        # result window
        res, resLen = [-1, -1], float("infinity")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # check if requirement satisfied
            if c in countT and window[c] == countT[c]:
                have += 1

            # when window is valid, shrink from the left
            while have == need:
                # update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                # remove leftmost char
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""