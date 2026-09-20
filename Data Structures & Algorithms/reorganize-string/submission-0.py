from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count how many times each character appears.
        count = Counter(s)

        # Python only has a min-heap, so use negative counts
        # to simulate a max-heap.
        #
        # Each heap item:
        # [negative_frequency, character]
        max_heap = [
            [-frequency, character]
            for character, frequency in count.items()
        ]

        heapq.heapify(max_heap)

        # Stores the character used in the previous round.
        # We temporarily keep it outside the heap so that
        # it cannot be selected twice in a row.
        previous = None

        result = ""

        # Continue while there is:
        # 1. A character in the heap, or
        # 2. A previously used character that still has copies left.
        while max_heap or previous:

            # A previous character still remains, but there is no
            # different character available to place between copies.
            if previous and not max_heap:
                return ""

            # Choose the character with the highest remaining frequency.
            frequency, character = heapq.heappop(max_heap)

            result += character

            # Since frequency is negative, adding 1 moves it toward zero.
            frequency += 1

            # The previous character can now go back into the heap
            # because we just used a different character.
            if previous:
                heapq.heappush(max_heap, previous)
                previous = None

            # If the current character still has copies remaining,
            # hold it outside the heap for one round.
            if frequency != 0:
                previous = [frequency, character]

        return result