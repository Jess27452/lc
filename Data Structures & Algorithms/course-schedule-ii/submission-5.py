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
#space between code
#overview of them problem at the beginning, figure out what courses we can take some course have prereq, brutal force+Solution(what the problem is)
#testcases: wrote comments each variable 
#time complexity/space complexity
#try google questions
#ask to run test cases: is it right, easiest way to save time by doing this, the way i imploement yhis si using dfs, this would give  a time compleixty of insetand of complexity for the burtal force.
#first, I will build adjency list and 
#test case
#test case 3 test cases(empty, easy, standard) #i have happy to run
