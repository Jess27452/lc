class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            current_sum = numbers[l] + numbers[r]

            if current_sum == target:
                # The problem asks for 1-indexed results, so we add 1 to our indices
                return [l + 1, r + 1]
            elif current_sum < target:
                # The sum is too small, make it bigger by moving the left pointer up
                l += 1
            else:
                # The sum is too big, make it smaller by moving the right pointer down
                r -= 1