class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prev_map={i:[] for i in range(numCourses)}
        for course,prev in prerequisites:
            prev_map[course].append(prev)
        visit=set()
        def dfs(course):
            if course in visit:
                return False
            if prev_map[course]==[]:
                return True
            visit.add(course)
            for nei in prev_map[course]:
                if not dfs(nei):
                    return False
            visit.remove(course)
            prev_map[course]=[]
            return True
        for course,prev in prerequisites:
            if not dfs(course):
                return False
        return True


        
