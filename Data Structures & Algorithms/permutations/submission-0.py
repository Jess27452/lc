class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # base case
        if len(nums) == 0:
            return [[]]

        # permutations of remaining numbers
        perms = self.permute(nums[1:])

        res = []

        # insert nums[0] into every position
        for p in perms:
            for i in range(len(p) + 1):

                p_copy = p.copy()

                p_copy.insert(i, nums[0])#creates fresh list before insertion.
                res.append(p_copy)

        return res