class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = left + (right - left) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                # middle might be the minimum, so do not remove it.
                right = middle

        return nums[left]