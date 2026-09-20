class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Characters currently inside the window.
        char_set = set()

        # Left boundary of the window.
        left = 0

        # Longest valid window found so far.
        result = 0

        # right expands the window.
        for right in range(len(s)):

            # If s[right] is already inside the window,
            # shrink the window from the left until
            # the duplicate is removed.
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Now s[right] is not duplicated.
            char_set.add(s[right])

            # Current window is from left through right.
            current_length = right - left + 1
            result = max(result, current_length)

        return result