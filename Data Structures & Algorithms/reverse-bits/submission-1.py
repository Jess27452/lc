class Solution:
    def reverseBits(self, n: int) -> int:
        # res will store the reversed binary number.
        res = 0

        # A 32-bit integer has positions 0 through 31.
        for i in range(32):

            # Move bit i of n to the far-right position,
            # then use & 1 to keep only that one bit.
            bit = (n >> i) & 1

            # Move that extracted bit to its reversed position.
            #
            # Original position i becomes position 31 - i:
            # 0  -> 31
            # 1  -> 30
            # 2  -> 29
            # ...
            # 31 -> 0
            #
            # | places this bit into res without changing
            # the bits already added.
            res = res | (bit << (31 - i))

        return res