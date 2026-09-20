class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        stack=[]
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                previ,prevh=stack.pop()
                maxArea=max(maxArea,prevh*(i-previ))
                start=previ
            stack.append((start,h))
        for i, h in stack:
              width=len(heights)-i
              maxArea = max(maxArea, h * width)
        return maxArea