class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,cur,total):
            if total==target:
                res.append(cur.copy())
                return
            if total>target:
                return
            for j in range(i, len(nums)):
                cur.append(nums[j])
                dfs(j,cur,total+nums[j])
                cur.pop()
        dfs(0,[],0)
        return res
        