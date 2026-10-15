class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        cur=[]
        nums.sort()
        
        def dfs(i,sum):
            if sum==target:
                res.append(cur.copy())
                return
            if sum>target:
                return
            for s in range(i,len(nums)):
                if s > i and nums[s] == nums[s-1]:#We only want to skip duplicates at the same recursion level, not duplicates across different levels.
                    continue
                cur.append(nums[s])
                dfs(s+1,sum+nums[s])
                cur.pop()
        dfs(0,0)
        return res
    