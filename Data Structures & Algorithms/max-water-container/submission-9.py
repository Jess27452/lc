class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater=0
        l=0
        r=len(heights)-1
        for i in range(len(heights)):
            if l>=r:
                break
            area=min(heights[l],heights[r])*(r-l)
            maxwater=max(maxwater,area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxwater
