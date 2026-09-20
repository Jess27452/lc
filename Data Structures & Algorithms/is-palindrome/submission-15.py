class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0:
            return True# don't need this since the large while loop already
            #handles this
            #if it's 0, left=0,right=-1, directly jumps to True
        left=0
        right=len(s)-1
        while left<right:
            while left <right and not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True