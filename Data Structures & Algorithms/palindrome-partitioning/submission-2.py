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
#eg;[1,1,2]
##dfs(2)（index 2)
##for j in range(2,3)

#j = 2 only

#DONE.
#now it go backs to 
#dfs(1)
#for j in range(1,3)

#j = 1
#j = 2

##So THIS loop continues later.
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