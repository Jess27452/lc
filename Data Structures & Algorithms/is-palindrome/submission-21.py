class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            # Skip non-letter/non-number characters on the left.
            while left < right and not self.alphaNum(s[left]):
                left += 1

            # Skip non-letter/non-number characters on the right.
            while left < right and not self.alphaNum(s[right]):
                right -= 1

            # Compare the two valid characters.
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers toward the center.
            left += 1
            right -= 1
#can also use [::-1] but built another string space o(n)
        return True

    def alphaNum(self, character: str) -> bool:
        return (
            ord("A") <= ord(character) <= ord("Z")
            or ord("a") <= ord(character) <= ord("z")
            or ord("0") <= ord(character) <= ord("9")
        )