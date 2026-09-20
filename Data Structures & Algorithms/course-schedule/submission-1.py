class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # HashMap: course -> list of prerequisites
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # HashSet: courses in current DFS path
        visitSet = set()

        def dfs(crs):
            # If course is already in current path, cycle exists
            if crs in visitSet:
                return False

            # If course has no prerequisites, it is safe
            if preMap[crs] == []:
                return True

            visitSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visitSet.remove(crs)
            ######we are rmoving because the node is no longer in the current recursion stack
            #A cycle means:
#we revisited a node BEFORE finishing it
#NOT:we visited it sometime in the past

#if we never remove:
#eg:graph:0 -> 1 -> 2 visitSet = {0,1,2}
#Later:dfs(1)checks:if 1 in visitSet
#True.
#Code incorrectly thinks:cycle exists But actually:1 was already safely finished earlier
#So removing is necessary.
            # Mark this course as already checked/safe
            preMap[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True