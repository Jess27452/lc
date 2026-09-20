class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Use 32 bits to imitate Java integer behavior.
        mask = 0xFFFFFFFF#11111111
        max_int = 0x7FFFFFFF#011111

        # b stores the carry that still needs to be added.
        while b != 0:
            # Find the carry using the OLD values of a and b.
            carry = ((a & b) << 1) & mask

            # XOR calculates the sum without carry.
            a = (a ^ b) & mask

            # Add the carry during the next loop.
            b = carry

        # Convert the 32-bit result back to a Python signed integer.
        if a <= max_int:
            return a              # already positive

        return ~(a ^ mask)        # convert negative 32-bit pattern