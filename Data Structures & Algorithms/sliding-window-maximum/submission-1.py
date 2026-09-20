class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        q=deque()
        l=r=0
        while r<len(nums):
            while q and nums[q[-1]]<nums[r]:#最后一个数比要进来的数小，pop掉，we want it keeps decreasing
                q.pop()
            q.append(r)
            if l>q[0]:
                q.popleft()
            if (r+1)>=k:# only helpful for first k that diddint reach size k
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output