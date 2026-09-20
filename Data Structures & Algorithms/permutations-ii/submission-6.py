class Solution:
    def permuteUnique(self, nums):
        res = []
        perm = []

        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        def dfs():
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            for n in count:

                if count[n]>0:
                    perm.append(n)
                    count[n]-=1
                    dfs()
                    perm.pop()
                    count[n]+=1
        dfs()
        return res
                                