class Solution:
    def reverse(self, x: int) -> int:
        max=0x7FFFFFFF
        min=-0x80000000
        res=0
        while x!=0:
            digit=int(math.fmod(x,10))
            x=int(x/10)
            if (res>max//10) or (res==max//10 and digit>max%10):
                return 0
            if (res<int(min/10)) or (res==int(min/10) and digit<-8):
                return 0
            res=res*10+digit
        return res