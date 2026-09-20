class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        prefix = suffix = 0

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            res = max(res, max(prefix, suffix))
        return res
        #Prefix alone assumes “build forward is enough”, but product arrays need both forward and backward views because negatives can completely change what is optimal.

        #Prefix scan asks:

#“What is the best thing I can build ending here?”

#Suffix scan asks:

#What is the best thing I can build starting here?”