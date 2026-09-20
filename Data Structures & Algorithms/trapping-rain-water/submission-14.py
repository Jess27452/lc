class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        lm=0
        rm=0
        water=0
        while l<r:
            if height[l]<=height[r]:
                lm=max(height[l],lm)
                water+=lm-height[l]
                l+=1
            else:
                rm=max(height[r],rm)
                water+=rm-height[r]
                r-=1
        return water 