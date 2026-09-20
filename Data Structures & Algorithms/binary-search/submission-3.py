class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)
        while left<right:
            middle=left+(right-left)//2
            if nums[middle] < target:
                left=middle+1
            elif nums[middle]==target:
                return middle
            else:
                right=middle
        return -1
