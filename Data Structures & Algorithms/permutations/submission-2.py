class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(i):
            if i==len(nums):
                res.append(nums.copy())
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                dfs(i+1)#i means the position we are filling, while j means which number we are trying in that position.
                nums[i],nums[j]=nums[j],nums[i]
        dfs(0)
        return res

                