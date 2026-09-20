class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r
        while l<=r:
            k=(l+r)//2
            hours=0
            for p in piles:
                hours+=math.ceil(p/k)
            if hours<=h:
                res=min(res,k)
                r=k-1#The problem is that k might equal r.is setting r=k , infite loop

            else:
                l=k+1
        return res 