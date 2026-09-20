from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            # We found the target.
            if nums[middle] == target:
                return True

            # Case 1: The left half is definitely sorted.
            if nums[left] < nums[middle]:

                # Target is inside the sorted left half.
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

            # Case 2: The right half is definitely sorted.
            elif nums[left] > nums[middle]:

                # Target is inside the sorted right half.
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

            # Case 3: nums[left] == nums[middle]
            # Duplicates make it impossible to determine
            # which half is sorted.
            else:
                left += 1
#Why is removing nums[left] safe?

#Before reaching this part, we already checked:

#f nums[middle] == target:
  ###  return True

#We know:

#nums[left] == nums[middle]

#Since nums[middle] was not the target, nums[left] is also not the target.
        return False