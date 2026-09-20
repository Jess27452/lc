from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp[i] stores the number of 1s
        # in the binary representation of i.
        #
        # We need answers for 0 through n,
        # so the list has n + 1 positions.
        dp = [0] * (n + 1)

        # offset stores the most recent power of 2.
        #
        # Powers of 2 are:
        # 1, 2, 4, 8, 16, ...
        #
        # Their binary forms contain exactly one 1:
        # 1  = 1
        # 2  = 10
        # 4  = 100
        # 8  = 1000
        offset = 1

        # Calculate answers for every number from 1 through n.
        for i in range(1, n + 1):

            # When i reaches the next power of 2,
            # update offset.
            #
            # Example:
            # offset = 2
            # offset * 2 = 4
            #
            # When i becomes 4, set offset = 4.
            if offset * 2 == i:
                offset = i

            # The current number i is made from:
            #
            # the leading 1 contributed by offset
            # +
            # the binary bits of i - offset
            #
            # Therefore:
            # number of 1s in i
            # = 1 + number of 1s in i - offset
            dp[i] = 1 + dp[i - offset]

        return dp    