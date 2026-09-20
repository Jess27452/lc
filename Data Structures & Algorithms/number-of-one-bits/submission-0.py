class Solution:
    def hammingWeight(self, n: int) -> int:
        #Why does subtracting 1 change the bits like this?

#Look at:

#n     = 1100
#n - 1 = 1011

#When you subtract 1 from a binary number:

#The rightmost 1 becomes 0.
#Every 0 after that rightmost 1 becomes 1.
        res = 0

        while n:
            # n & 1 checks whether the rightmost binary digit is 1.
            if n & 1:
                res += 1

            # Remove the rightmost binary digit.
            n = n >> 1

        return res