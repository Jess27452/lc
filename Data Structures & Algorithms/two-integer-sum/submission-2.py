from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # number: index

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[n] = i
        #return [] 
        #However, the LeetCode Two Sum problem guarantees that exactly one valid answer exists, so the final return [] is usually unnecessary.
        # time and space:o(n)