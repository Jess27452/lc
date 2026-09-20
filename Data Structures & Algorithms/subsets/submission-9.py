class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(start):
            res.append(subset.copy())
            for i in range(start,len(nums)):
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()
        dfs(0)
        return res