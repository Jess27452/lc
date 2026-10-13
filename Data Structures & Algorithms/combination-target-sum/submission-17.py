class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def bt(i,cur,total):
            if total==target:
                res.append(cur.copy())
                return
            if i>=len(nums) or total>target:
                return
            cur.append(nums[i])
            bt(i,cur,total+nums[i])
            cur.pop()
            bt(i+1,cur,total)
        bt(0,[],0)
        return res
            
                
                
                
                
            
            