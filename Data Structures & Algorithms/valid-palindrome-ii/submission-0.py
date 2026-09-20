class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Try deleting the left character.
                skip_left = s[left + 1:right + 1]

                # Try deleting the right character.
                skip_right = s[left:right]

                return (
                    skip_left == skip_left[::-1] # it reverses the string.
                    or skip_right == skip_right[::-1]
                )

            left += 1
            right -= 1

        return True