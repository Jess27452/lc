class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        lmax=0
        rmax=0
        water=0
        while left<right:
            if height[left]<=height[right]:
                lmax=max(height[left],lmax)
                water+=lmax-height[left]
                left+=1
            else:
                rmax=max(height[right],rmax)
                water+=rmax-height[right]
                right-=1
        return water 