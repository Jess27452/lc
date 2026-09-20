class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is "0", the product is always "0".
        if "0" in [num1, num2]:
            return "0"

        # If num1 has m digits and num2 has n digits,
        # their product can have at most m + n digits.
        #
        # Example:
        # 99 has 2 digits
        # 99 has 2 digits
        # 99 × 99 = 9801, which has 4 digits
        #
        # res stores the answer digits in reverse order.
        res = [0] * (len(num1) + len(num2))

        # Reverse both strings so index 0 is the ones digit.
        #
        # "123" becomes "321"
        #
        # Index:
        # 0 = ones place
        # 1 = tens place
        # 2 = hundreds place
        num1 = num1[::-1]
        num2 = num2[::-1]

        # Multiply every digit in num1 by every digit in num2.
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                # Multiply the two current digits.
                digit = int(num1[i1]) * int(num2[i2])

                # The product belongs at position i1 + i2.
                #
                # ones × ones       → position 0
                # ones × tens       → position 1
                # tens × ones       → position 1
                # tens × tens       → position 2
                res[i1 + i2] += digit

                # Move the carry to the next position.
                #
                # Example:
                # If res[current] becomes 18:
                # carry = 18 // 10 = 1
                res[i1 + i2 + 1] += res[i1 + i2] // 10

                # Keep only the current position's final digit.
                #
                # 18 % 10 = 8
                res[i1 + i2] %= 10

        # res is currently in reverse order,
        # so reverse it back to normal order.
        res = res[::-1]

        # Skip unnecessary leading zeroes.
        beginning = 0

        while beginning < len(res) and res[beginning] == 0:
            beginning += 1

        # Convert every integer digit into a string.
        res = map(str, res[beginning:])

        # Join the separate characters into one string.
        return "".join(res)