class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub=nums[0]
        curSum=0
        for a in nums:
            if curSum<0:
                curSum=0
            curSum+=a
            maxSub=max(curSum,maxSub)
        return maxSub