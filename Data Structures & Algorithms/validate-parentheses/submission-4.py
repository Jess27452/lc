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
            
             top=stack.pop()
             if top!=match[ch]:
                 return False
          else:
             stack.append(ch)
    
        return len(stack)== 0

            
        