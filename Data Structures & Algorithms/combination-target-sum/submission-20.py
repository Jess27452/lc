class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        cur=[]
        def dfs(i,sum):
            if sum==target:
                res.append(cur.copy())
                return
            if sum>target:
                return
            for s in range(i,len(nums)):
                cur.append(nums[s])
                dfs(s,sum+nums[s])
                cur.pop()
        dfs(0,0)
        return res
