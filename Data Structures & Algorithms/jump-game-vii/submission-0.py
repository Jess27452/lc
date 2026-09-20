from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        # Queue stores positions that we KNOW are reachable.
        # We start at index 0.
        q = deque([0])

        # farthest = farthest index that we have already checked.
        # This prevents us from checking the same indices again and again.
        farthest = 0

        while q:
            # Take one reachable position from the queue.
            i = q.popleft()

            # Normally, from i, we can start checking at:
            # i + minJump
            #
            # BUT we may have already checked some positions before.
            # farthest + 1 = first position we have NOT checked yet.
            #
            # So choose whichever is larger.
            start = max(i + minJump, farthest + 1)

            # We can jump at most to:
            # i + maxJump
            #
            # +1 is needed because range() excludes the right boundary.
            # len(s) prevents us from going outside the string.
            end = min(i + maxJump + 1, len(s))

            # Check every possible new landing position.
            for j in range(start, end):

                # We can only land on "0".
                if s[j] == "0":

                    # j is reachable, so add it to the queue.
                    q.append(j)

                    # If j is the last index, we succeeded.
                    if j == len(s) - 1:
                        return True

            # We have now checked everything up to i + maxJump.
            farthest = i + maxJump
#from 0 → check 2,3
#from 2 → check 4,5
#from 3 → check 5,6    ← 5 checked AGAIN
#from 4 → check 6      ← 6 checked AGAIN
        # Queue became empty and we never reached the last index.
        return False