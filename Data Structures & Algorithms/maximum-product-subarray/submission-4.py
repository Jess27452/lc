class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # current max product ending here
        curMax = 1
        # current min product ending here (important for negatives)
        curMin = 1

        res = max(nums)

        for n in nums:

            # if we hit zero, reset
            if n == 0:
                curMax, curMin = 1, 1
                res = max(res, 0)
                continue

            # store previous curMax before updating
            tmp = curMax * n

            # update curMax and curMin
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)

            # update result
            res = max(res, curMax)

        return res

        #curMax = best product that must touch current position
#res = best product anywhere