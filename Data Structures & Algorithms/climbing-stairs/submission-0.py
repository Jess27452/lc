class Solution:
    def climbStairs(self, n: int) -> int:
        # one means: number of ways to reach the current step - 1
        # two means: number of ways to reach the current step - 2
        #
        # For n = 1, there is 1 way:
        # 1
        #
        # For n = 2, there are 2 ways:
        # 1 + 1
        # 2
        one, two = 1, 1

        # We loop n - 1 times because we already know the base starting values.
        #
        # Example:
        # n = 5
        # We need to calculate up to step 5.
        # Starting:
        # one = 1
        # two = 1
        #
        # Each loop moves one step forward.
        for i in range(n - 1):
            # Save old one before changing it.
            # Because we still need old one to update two.
            temp = one

            # New one becomes:
            # ways to previous step + ways to step before previous
            #
            # This is the main formula:
            # ways(n) = ways(n - 1) + ways(n - 2)
            one = one + two

            # Move two forward.
            # two becomes the old one.
            two = temp

        # After the loop, one stores the answer.
        return one