class Solution:
    def isHappy(self, n: int) -> bool:
        # visit stores every number we have already seen.
        #
        # This helps us detect a cycle.
        # If the same number appears again, the sequence
        # will repeat forever and never reach 1.
        visit = set()

        # Continue while n has not appeared before.
        while n not in visit:
            # Remember the current number.
            visit.add(n)

            # Replace n with the sum of the squares of its digits.
            n = self.sumOfSquares(n)

            # If the sequence reaches 1,
            # n is a happy number.
            if n == 1:
                return True

        # If the loop stops, n was already in visit.
        # This means the sequence entered a cycle.
        return False

    def sumOfSquares(self, n: int) -> int:
        # output stores the total sum of squared digits.
        output = 0

        # Process every digit of n.
        while n:
            # Get the last digit.
            #
            # Example:
            # 123 % 10 = 3
            digit = n % 10

            # Square the digit.
            #
            # Example:
            # digit = 3
            # digit ** 2 = 9
            digit = digit ** 2

            # Add the squared digit to the total.
            output += digit

            # Remove the last digit from n.
            #
            # Example:
            # 123 // 10 = 12
            n = n // 10

        return output