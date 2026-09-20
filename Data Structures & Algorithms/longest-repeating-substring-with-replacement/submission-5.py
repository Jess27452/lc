class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Frequency of each character inside the current window.
        count = {}

        # Longest valid window found.
        res = 0

        # Left boundary of the sliding window.
        left = 0

        # Highest frequency of one character in the window.
        max_frequency = 0

        # right is the right boundary of the window.
        for right in range(len(s)):
            # Add s[right] to the current window.
            count[s[right]] = 1 + count.get(s[right], 0)

            # Update the frequency of the most common character.
            max_frequency = max(
                max_frequency,
                count[s[right]]
            )

            # Number of replacements needed:
            #
            # window size - most frequent character count
            if (
                (right - left + 1) - max_frequency > k
            ):
                # Remove the leftmost character from the window.
                count[s[left]] -= 1
                left += 1

            # The window is valid now.
            res = max(
                res,
                right - left + 1
            )

        return res