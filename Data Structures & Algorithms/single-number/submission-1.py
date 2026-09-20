from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Store the running XOR result.
        #
        # We start with 0 because:
        # 0 ^ x = x
        res = 0

        # Visit every number in the list.
        for n in nums:
            # XOR the current number with the running result.
            #
            # Important XOR rules:
            # x ^ x = 0        → duplicate numbers cancel out
            # x ^ 0 = x        → XOR with 0 keeps the number
            #
            # This line can also be written as:
            # res ^= n
            res = n ^ res

        # After all duplicate pairs cancel out,
        # res contains the number that appears only once.
        return res
        #Different numbers may have some matching bits that cancel, but the whole numbers do not disappear unless they are identical.