class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        cur=[]
        candidates.sort()
        def dfs(i,total):
            if target==total:
                res.append(cur.copy())
                return
            if i == len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i+1,total+candidates[i])
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i=i+1
            cur.pop()
            dfs(i+1,total)
        dfs(0,0)
        return res