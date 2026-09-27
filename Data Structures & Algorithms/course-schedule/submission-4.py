class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap={i:[] for i in range(numCourses)}
        for crs,preq in prerequisites:
            prevMap[crs].append(preq)
        visitSet=set()
        def dfs(crs):
            if prevMap[crs]==[]:
                return True 
            if crs in visitSet:
                return False
            visitSet.add(crs)
            for nei in prevMap[crs]:
                if not dfs(nei):
                    return False
            visitSet.remove(crs)
            prevMap[crs]=[]
            return True
        for crs, preq in prerequisites:
            if not dfs(crs):
                return False
        return True
