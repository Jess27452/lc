class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            # Get the rightmost bit of n
            bit = n & 1

            # Shift res left to make space,
            # then put the new bit in
            res = (res << 1) | bit

            # Remove the rightmost bit from n
            n >>= 1

        return res