class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        lm=height[0]
        rm=height[len(height)-1]
        water=0
        while l<r:
            if height[l]<height[r]:#Compare the current two bars only.
            #If current left bar is lower than current right bar,
#then the right side already has a wall tall enough for left,
#so it is safe to process left.
                lm=max(lm,height[l])
                water+=lm-height[l]
                l+=1
            else:
                rm=max(rm,height[r])
                water+=rm-height[r]
                r-=1
        return water
        #example 5,1,4 still works because
        #l=0, r=2
#height[l]=5, height[r]=4

#5 < 4? no
#process right

#######using lm and rm directly follows:water = min(leftMax, rightMax) - height[i]