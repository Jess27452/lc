class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))

        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit1 = ord(num1[i]) - ord("0")
                digit2 = ord(num2[j]) - ord("0")

                res[i + j] += digit1 * digit2

                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10

        res = res[::-1]

        while len(res) > 1 and res[0] == 0:
            res.pop(0)

        return "".join(str(digit) for digit in res)