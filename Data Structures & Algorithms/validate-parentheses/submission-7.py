class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        match={")":"(",  
               ']': '[',
               '}': '{'
        }
        for ch in s:
            if ch in match:
                if not stack:
                    return False
                new=stack.pop()
                if new!=match[ch]:
                    return False
            else:
                stack.append(ch)
        ###we can't do return True
        ##since if s = "(("
        ##the. it always return true
        return len(stack) == 0