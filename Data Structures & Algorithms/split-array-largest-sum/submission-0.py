from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        def canSplit(largest: int) -> bool:
            # Number of subarrays currently being used.
            subarrays = 1

            # Sum of the current subarray.
            current_sum = 0

            for number in nums:
                current_sum += number

                # Current subarray became too large.
                if current_sum > largest:
                    # Start a new subarray with this number.
                    subarrays += 1
                    current_sum = number

            # We can use this maximum if we need
            # no more than m subarrays.
            return subarrays <= m

        # Smallest possible answer:
        # at least the largest individual number.
        left = max(nums)

        # Largest possible answer:
        # put every number into one subarray.
        right = sum(nums)

        result = right

        while left <= right:
            middle = left + (right - left) // 2

            if canSplit(middle):
                # middle is possible, so save it.
                result = middle

                # Try to find a smaller possible maximum.
                right = middle - 1

            else:
                # middle is too small.
                # We need to allow a larger subarray sum.
                left = middle + 1

        return result

        #Let:

#n be the number of elements
#S = sum(nums)
#M = max(nums)

#canSplit() scans the whole array:

#O(n)

#Binary search examines the answer range from M to S:

#O(log(S - M))

#Total time:

#O(n log(S - M))

#Extra space:

#O(1