from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)

        target = sum(nums) // 2
        #if equal to target then the remaining automatically equal to target

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            #the reason for nextDP is:
#to make sure each number is used at most once, and to safely build the next set of possible sums.

            for t in dp:
                if t + nums[i] == target:
                    return True

                nextDP.add(t + nums[i])  # take nums[i]
                nextDP.add(t)            # don't take nums[i]

            dp = nextDP

        return target in dp