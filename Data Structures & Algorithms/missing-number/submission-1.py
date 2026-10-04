from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]

        return res