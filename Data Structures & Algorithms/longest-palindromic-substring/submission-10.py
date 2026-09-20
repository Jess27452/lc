class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        maxlen=1
        start=0
        for i in range(n):
            dp[i][i]=True
            start=i
            maxlen=1
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                start=i
                maxlen=2
        for length in range(3, n + 1):
            for left in range(n - length + 1):
                right=left+length-1
                if s[left]==s[right] and dp[left+1][right-1]==True:
                    dp[left][right]=True

                    if length > maxlen:
                        start = left
                        maxlen = length
         
        return s[start:start + maxlen]           