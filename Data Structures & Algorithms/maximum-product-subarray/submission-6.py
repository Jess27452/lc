class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Overall maximum product seen so far
        res = max(nums)

        # curMax = maximum product ending at current index
        # curMin = minimum product ending at current index
        # We keep curMin because a negative number can turn it into a new maximum
        curMin, curMax = 1, 1

        for n in nums:
            # If n is 0, any product crossing this point becomes 0,
            # so reset for a new subarray
            if n == 0:
                curMin, curMax = 1, 1
                continue

            # Save old curMax because curMax will be updated first
            tmp = curMax * n

            # Current maximum can come from:
            # 1. old curMax * n
            # 2. old curMin * n (negative * negative can become large positive)
            # 3. start a new subarray with n
            curMax = max(n * curMax, n * curMin, n)

            # Current minimum can come from the same three choices
            curMin = min(tmp, n * curMin, n)

            # Update the best product found anywhere
            res = max(res, curMax)

        return res