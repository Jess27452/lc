from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1
        i = 0

        def swap(index1, index2):
            temp = nums[index1]
            nums[index1] = nums[index2]
            nums[index2] = temp

        while i <= right:
            if nums[i] == 0:
                swap(i, left)
                left += 1
                i += 1

            elif nums[i] == 2:
                swap(i, right)
                right -= 1

            else:
                # nums[i] == 1
                i += 1