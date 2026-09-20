class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack = []
        for i,v in enumerate(temperatures):
            while stack and v>stack[-1][0]:
                pret,prei=stack.pop()
                result[prei]=i-prei
            stack.append([v,i])

        return result