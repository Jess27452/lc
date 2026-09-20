class Solution:
    def rob(self, nums: List[int]) -> int:
        # If there is only one house, we must rob it
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses: List[int]) -> int:
            # prev2 = best answer up to house i-2
            # prev1 = best answer up to house i-1
            prev2 = 0
            prev1 = 0

            for money in houses:
                # Two choices at each house:
                #
                # 1. Skip this house
                #    -> keep the best total from previous house = prev1
                #
                # 2. Rob this house
                #    -> then we cannot rob the previous house,
                #       so add current money to best total from i-2 = money + prev2
                #
                # Take whichever is larger
                curr = max(prev1, money + prev2)

                # Move the window forward:
                # old prev1 becomes new prev2
                prev2 = prev1

                # current best becomes new prev1
                prev1 = curr

            # prev1 always stores the best answer up to the current house
            return prev1

        # Because first and last houses are adjacent in a circle,
        # we cannot rob both.
        #
        # So solve two separate linear cases:
        # 1. Use houses 0 to n-2  -> nums[:-1]
        # 2. Use houses 1 to n-1  -> nums[1:]
        #
        # The answer is the larger of the two.
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))