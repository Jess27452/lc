class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
#For every index, try to grow a palindrome around it.
#Check odd palindromes.
#Check even palindromes. ######check even and odd for every index
#Whenever we find a longer one, save it.
#Return the longest saved palindrome.
        for i in range(len(s)):
            # odd length palindrome
            
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res