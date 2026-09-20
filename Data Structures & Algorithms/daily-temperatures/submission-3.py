class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][1]:
                stacknd,stackT=stack.pop()
                res[stacknd]=i-stacknd
            stack.append((i,t))
        return res

            