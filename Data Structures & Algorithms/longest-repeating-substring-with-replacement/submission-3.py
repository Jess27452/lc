class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        l=0
        maxcount=0
        best=0
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            maxcount=max(maxcount,count[s[r]])
            while (r-l+1)-maxcount>k:
                count[s[l]]-=1#We're removing one character from the window, so its count decreases by 1.
                l+=1#should be l+=1 since we are moving left pointer to right
            best=max(best,r-l+1)
        return best