class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xFFFFFFFF
        max=0x7FFFFFFF
        while b!=0:
            carry = ((a & b) << 1) & mask
            a=(a^b)& mask
            b=carry
        if a <=max:
            return a
        return ~(a ^ mask)