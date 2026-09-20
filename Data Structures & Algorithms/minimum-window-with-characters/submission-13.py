from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If t is empty or longer than s,
        # no valid window can exist.
        if not t or len(t) > len(s):
            return ""

        # countT stores how many times each character
        # must appear in the window.
        #
        # Example:
        # t = "AABC"
        # countT = {"A": 2, "B": 1, "C": 1}
        countT = Counter(t)

        # window stores character frequencies
        # inside the current window s[left:right + 1].
        window = {}

        # Number of distinct character requirements
        # currently satisfied.
        have = 0

        # Total number of distinct character requirements.
        #
        # Example:
        # t = "AABC"
        # need = 3 because we need A, B, and C.
        need = len(countT)

        # Save the starting and ending indices
        # of the smallest valid window.
        result = [-1, -1]

        # Length of the smallest valid window found so far.
        result_length = float("inf")

        # Left side of the sliding window.
        left = 0

        # Move right through the string to expand the window.
        for right in range(len(s)):
            current_character = s[right]

            # Add the current character to the window.
            window[current_character] = (
                window.get(current_character, 0) + 1
            )

            # If this character is required and we now have
            # exactly the required number of copies,
            # one character requirement is satisfied.
            if (
                current_character in countT
                and window[current_character]
                == countT[current_character]
            ):
                have += 1

            # If have == need, the current window contains
            # every required character.
            #
            # Try to shrink the window from the left while
            # keeping it valid.
            while have == need:
                current_length = right - left + 1

                # Update the result if this window is smaller
                # than the smallest valid window found before.
                if current_length < result_length:
                    result = [left, right]
                    result_length = current_length

                # Remove the leftmost character from the window.
                left_character = s[left]
                window[left_character] -= 1

                # If we removed a required character and now
                # have fewer copies than required, the window
                # is no longer valid.
                if (
                    left_character in countT
                    and window[left_character]
                    < countT[left_character]
                ):
                    have -= 1

                # Move the left boundary to the right.
                left += 1

        # If result_length is still infinity,
        # no valid substring was found.
        if result_length == float("inf"):
            return ""

        start, end = result

        # Python slicing excludes the ending index,
        # so use end + 1.
        return s[start:end + 1]