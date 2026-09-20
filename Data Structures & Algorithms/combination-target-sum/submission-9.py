class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def bt(start, total):
            if total == target:
                res.append(cur.copy())
                return

            if total > target:
                return

            for i in range(start, len(nums)):
                cur.append(nums[i])

                bt(i, total + nums[i])

                cur.pop()

        bt(0, 0)
        return res