#6/3
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l=0
        r=len(height)-1
        lm=0
        rm=0
        water=0
        while l<r:
            if height[l]<height[r]:
                lm=max(lm,height[l])
                water+=lm-height[l]
                l+=1
            else:
                rm=max(rm,height[r])
                water+=rm-height[r]
                r-=1
        return water
#If you use height[l] < height[r]:
   # lm/rm can start at 0

#If you use lm < rm:
    #lm/rm should start as height[l] and height[r]