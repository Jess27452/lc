class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={}
        for i, n in enumerate(nums):
            if target-n in prevMap:
                return [prevMap[target-n],i]
            prevMap[n]=i
