class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []      # stores final answers
        part = []     # current partition path

        # check whether s[l:r] is palindrome
        def isPali(l, r):

            while l < r:

                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1

            return True

        def dfs(i):

            # BASE CASE
            # reached end of string
            #At every index:
#i
#we ask:
#How far should this substring extend?
            if i >= len(s):

                # copy current partition into result
                res.append(part.copy())
                return

            # TRY EVERY SUBSTRING STARTING AT i
            for j in range(i, len(s)):

                # skip invalid palindrome
                if not isPali(i, j):
                    continue

                # MAKE CHOICE
                # choose substring s[i:j+1]
                part.append(s[i:j+1])

                # RECURSE
                # continue from next index
                dfs(j + 1)

                # UNDO CHOICE (BACKTRACK)
                part.pop()

        dfs(0)

        return res