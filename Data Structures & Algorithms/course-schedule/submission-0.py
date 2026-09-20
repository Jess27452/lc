
        #O(n+p)
        # since Because in this problem we treat it like a graph:

#n = number of courses = number of nodes

#p = number of prerequisite pairs = number of edges
#visitSet = current chain of unfinished calls

#if crs in visitSet = “I looped back to something unfinished” → cycle

#if not dfs(pre) = “my prerequisite failed, so I fail too”
# and we ned to chec if not dfs(pre):return fasle because if we dont check, if any of the rperequriest returnf alse
#we will ignore that


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # -------------------------------------------------
        # Step 1: Build the graph
        #
        # preMap[course] = list of prerequisites for that course
        #
        # Example:
        # prerequisites = [[0,1], [1,2]]
        #
        # means:
        #   to take 0, you need 1 first
        #   to take 1, you need 2 first
        #
        # so:
        #   preMap = {
        #       0: [1],
        #       1: [2],
        #       2: []
        #   }
        # -------------------------------------------------
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # -------------------------------------------------
        # visitSet stores the courses in the CURRENT DFS PATH
        #
        # This is NOT "all visited nodes forever".
        #
        # It only means:
        # "these are the courses currently being explored
        #  in this recursive chain"
        #
        # If during DFS we try to visit a course that is
        # already in this set, then we found a cycle.
        # -------------------------------------------------
        visitSet = set()

        def dfs(crs: int) -> bool:
            # -------------------------------------------------
            # QUESTION YOU ASKED:
            # Why do we do:
            #     if crs in visitSet: return False
            #
            # Because this detects a cycle.
            #
            # Example:
            #   0 needs 1
            #   1 needs 2
            #   2 needs 0
            #
            # DFS path:
            #   dfs(0) -> dfs(1) -> dfs(2) -> dfs(0)
            #
            # When we reach dfs(0) again, 0 is already in visitSet,
            # which means we came back to something already in the
            # current path.
            #
            # That is exactly a cycle.
            # -------------------------------------------------
            if crs in visitSet:
                return False

            # -------------------------------------------------
            # If this course has no prerequisites left,
            # then it is safe / finishable.
            #
            # This can happen in 2 ways:
            #
            # 1. It originally had no prerequisites
            # 2. We already checked it before and marked it safe
            #    by doing preMap[crs] = []
            # -------------------------------------------------
            if preMap[crs] == []:
                return True

            # -------------------------------------------------
            # Add this course to the current DFS path
            #
            # Example:
            # if we are checking course 0, then course 0 is now
            # "active" in the recursion path.
            # -------------------------------------------------
            visitSet.add(crs)

            # -------------------------------------------------
            # Check all prerequisites of this course
            #
            # QUESTION YOU ASKED:
            # Why do we need:
            #     if not dfs(pre): return False
            #
            # Even though inside dfs there is already a
            # "return False"?
            #
            # Answer:
            # because a False found DEEPER in recursion must be
            # passed back UP to the caller.
            #
            # Example:
            #   dfs(0)
            #      dfs(1)
            #         dfs(2)
            #            dfs(0)  -> returns False
            #
            # That False only returns from the INNERMOST call.
            # Now dfs(2) must notice that failure and also return False.
            # Then dfs(1) must also return False.
            # Then dfs(0) must also return False.
            #
            # That "bubbling up" is exactly what this line does:
            #     if not dfs(pre): return False
            #
            # So:
            # - if crs in visitSet: return False
            #       = detects the cycle
            #
            # - if not dfs(pre): return False
            #       = propagates the failure upward
            # -------------------------------------------------
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # -------------------------------------------------
            # If we finished checking all prerequisites and none
            # caused a cycle, then we are done exploring this course.
            #
            # Remove it from current DFS path because recursion
            # is backing out now.
            # -------------------------------------------------
            visitSet.remove(crs)

            # -------------------------------------------------
            # Mark this course as safe.
            #
            # This is memoization.
            #
            # It means:
            # "we already verified that this course can be finished,
            # so next time return True immediately."
            # -------------------------------------------------
            preMap[crs] = []

            return True

        # -------------------------------------------------
        # We must try DFS from every course.
        #
        # Why?
        # Because the graph may have disconnected parts.
        #
        # Example:
        #   0 -> 1    (safe)
        #   3 -> 4
        #   4 -> 3    (cycle)
        #
        # If we only started from 0, we would miss the cycle
        # in the other component.
        # -------------------------------------------------
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True