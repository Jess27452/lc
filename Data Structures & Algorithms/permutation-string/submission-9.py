class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s2 cannot contain a substring of length len(s1)
        # when s1 is longer than s2.
        if len(s1) > len(s2):
            return False

        # Store counts for the 26 lowercase English letters.
        s1_count = [0] * 26
        s2_count = [0] * 26

        # Count:
        # 1. Every character in s1
        # 2. Every character in the first window of s2
        for i in range(len(s1)):
            s1_index = ord(s1[i]) - ord("a")
            s2_index = ord(s2[i]) - ord("a")

            s1_count[s1_index] += 1
            s2_count[s2_index] += 1

        # matches tells us how many of the 26 character
        # frequencies are currently equal.
        matches = 0

        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        # Left side of the current sliding window.
        left = 0

        # right starts after the first window because
        # the first len(s1) characters were already counted.
        for right in range(len(s1), len(s2)):

            # If all 26 frequencies match, the current window
            # is a permutation of s1.
            if matches == 26:
                return True

            # ---------------------------------
            # Add s2[right] to the window
            # ---------------------------------
            index = ord(s2[right]) - ord("a")
            s2_count[index] += 1

            # After increasing the count, the frequencies
            # may have become equal.
            if s1_count[index] == s2_count[index]:
                matches += 1

            # After increasing, s2_count is now one larger
            # than s1_count. This means they were equal before
            # the increase, so we lost one match.
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1

            # ---------------------------------
            # Remove s2[left] from the window
            # ---------------------------------
            index = ord(s2[left]) - ord("a")
            s2_count[index] -= 1

            # After decreasing the count, they may now be equal.
            if s1_count[index] == s2_count[index]:
                matches += 1

            # After decreasing, s2_count is now one smaller
            # than s1_count. This means they were equal before
            # the decrease, so we lost one match.
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1

            # Move the left side forward.
            left += 1

        # Check the final window.
        return matches == 26