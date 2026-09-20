class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        # The product can have at most m + n digits.
        # The digits here are stored in normal order.
        result = [0] * (m + n)

        # Start from the rightmost digits.
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])

                # The product contributes to two adjacent positions.
                carry_position = i + j
                digit_position = i + j + 1

                # Add the new product to anything already stored
                # at the lower position.
                total = product + result[digit_position]

                # Keep the ones digit in the lower position.
                result[digit_position] = total % 10

                # Send the carry to the position on the left.
                result[carry_position] += total // 10

        # Convert digits into one string and remove leading zeroes.
        answer = "".join(map(str, result)).lstrip("0")

        return answer or "0"