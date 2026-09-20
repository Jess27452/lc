class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x: float, n: int) -> float:
            # If the base is 0, every positive power is 0.
            if x == 0:
                return 0

            # Any nonzero number raised to power 0 is 1.
            #
            # Example:
            # 5^0 = 1
            if n == 0:
                return 1

            # Square x and divide n by 2.
            #
            # Example:
            # 2^8 = 4^4 = 16^2 = 256^1
            #
            # This makes n much smaller during every recursive call.
            res = helper(x * x, n // 2)

            # If n is odd, one extra x is needed.
            #
            # Odd:
            # x^5 = x * (x^2)^2
            #
            # Even:
            # x^4 = (x^2)^2
            if n % 2 == 1:
                return x * res
            else:
                return res

        # helper works with a nonnegative exponent.
        #
        # If n = -3, abs(n) = 3.
        res = helper(x, abs(n))

        # Positive exponent:
        # x^3 stays x^3.
        #
        # Negative exponent:
        # x^-3 = 1 / x^3.
        if n >= 0:
            return res
        else:
            return 1 / res