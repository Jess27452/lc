class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prev_map = {i: [] for i in range(numCourses)}
        for course, prev in prerequisites:
            prev_map[course].append(prev)

        visit=set()
        res=[]
        
        def dfs(course):
            if course in visit:
                return False
            if prev_map[course] == []:
                if course not in res:
                    res.append(course)
                return True
            visit.add(course)
            for nei in prev_map[course]:
                if not dfs(nei):
                    return False
            visit.remove(course)
            prev_map[course] = []
            if course not in res:
                    res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return res