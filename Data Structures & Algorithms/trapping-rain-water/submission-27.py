class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l=0
        r=len(height)-1
        leftmax=height[l]
        rightmax=height[r]
        res=0
        #At this position, either update max wall, or trap water using old max wall.
        while l<r:
            if leftmax<rightmax:
                l+=1
                leftmax=max(leftmax,height[l])
                res+=leftmax-height[l]
                #if putting l+=1 here, 
                #Problem: you compare leftmax < rightmax before updating leftmax.
            else:
                r-=1
                rightmax=max(rightmax,height[r])
                res+=rightmax-height[r]
        return res 