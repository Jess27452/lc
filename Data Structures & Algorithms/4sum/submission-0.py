from typing import List


class Solution:
    def fourSum(
        self,
        nums: List[int],
        target: int
    ) -> List[List[int]]:

        nums.sort()

        result = []
        current = []

        def k_sum(k: int, start: int, remaining_target: int) -> None:
            # Recursive case: reduce k-Sum to (k - 1)-Sum.
            if k != 2:
                for i in range(start, len(nums) - k + 1):

                    # Skip duplicate choices at this recursion level.
                    if i > start and nums[i] == nums[i - 1]:
                        continue

                    # Choose nums[i].
                    current.append(nums[i])

                    # Find the remaining k - 1 numbers.
                    k_sum(
                        k - 1,
                        i + 1,
                        remaining_target - nums[i]
                    )

                    # Undo the choice before trying another value.
                    current.pop()

                return

            # Base case: solve 2Sum using two pointers.
            left = start
            right = len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum < remaining_target:
                    left += 1

                elif current_sum > remaining_target:
                    right -= 1

                else:
                    result.append(
                        current + [nums[left], nums[right]]
                    )

                    left += 1
                    right -= 1

                    # Skip duplicate left values.
                    while (
                        left < right
                        and nums[left] == nums[left - 1]
                    ):
                        left += 1

                    # Skip duplicate right values.
                    while (
                        left < right
                        and nums[right] == nums[right + 1]
                    ):
                        right -= 1

        k_sum(4, 0, target)

        return result