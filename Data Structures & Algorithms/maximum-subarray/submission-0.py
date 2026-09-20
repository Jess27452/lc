class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0#the best subarray sum ending at the current position.

        for n in nums:
            if curSum < 0:#If the previous sum is negative, throw it away.
                curSum = 0#a negative sum will only make the next subarray worse.
            curSum += n
            maxSub = max(maxSub, curSum)

        return maxSub