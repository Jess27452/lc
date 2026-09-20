class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        stack=[]
        for i, h in enumerate(heights):
            start=i
            while stack and h<stack[-1][1]:# we use while here since every taller
            #one should end here
            #The rectangle represented by the taller bar
#can no longer extend to the right.
                index,height=stack.pop()
                max_area=max(max_area, height*(i-index))
                start=index
            stack.append((start,h))#we need to push (start,h) 
            #instead of (i,h) since start represent where this 
            #hieght can go to the left, after popping

        for index, height in stack:
             max_area = max(max_area, height * (len(heights) - index))
    #can extend all of the way to the end so we use len(heights)
        return max_area     
    #some heights never encounter a smaller bar,
#so they never get popped during traversal.          
        