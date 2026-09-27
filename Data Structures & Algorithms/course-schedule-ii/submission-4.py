class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #describe brutal force
        #how it's better than brutal force, why optimal
        #time complexity for both brutal force and optimal Solution
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

       #{0:[],1:[0],2:[]}
       #visit:{}
       #res:[0，1，2]