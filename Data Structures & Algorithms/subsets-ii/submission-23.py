class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        cur=[]
        nums.sort()
        def dfs(i):
            res.append(cur.copy())
            for s in range(i,len(nums)):
                if s>i and nums[s]==nums[s-1]:
                    continue
                cur.append(nums[s])
                dfs(s+1)
                cur.pop()
        dfs(0)
        return res


