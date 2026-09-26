class Solution:
    def jump(self, nums: List[int]) -> int:
        res=0
        l=0
        r=0
        while r<len(nums)-1:
            farthest=0#that’s okay because each while loop represents one new jump level.
#We only care about the farthest place reachable from the current range [l, r].
            for i in range(l,r+1):
                farthest=max(farthest,i+nums[i])
            l=r+1
            r=farthest
            res+=1
        return res