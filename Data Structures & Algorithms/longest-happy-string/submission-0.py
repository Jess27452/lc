import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = ""
        max_heap = []

        # Python has a min-heap, so store negative counts
        # to simulate a max-heap.
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(max_heap, (count, char))

        while max_heap:
            # Take the character with the largest remaining count.
            count, char = heapq.heappop(max_heap)

            # If using this character would create three identical
            # characters in a row, use the second-most frequent one.
            if (
                len(result) > 1
                and result[-1] == result[-2] == char
            ):
                # There is no other character available.
                if not max_heap:
                    break
#This is different from Reorganize String, where the problem requires using every character. In that problem, if all characters cannot be used, we return "".
                count2, char2 = heapq.heappop(max_heap)

                result += char2

                # We used one char2.
                count2 += 1

                # Put char2 back if copies remain.
                if count2 != 0:
                    heapq.heappush(max_heap, (count2, char2))

            else:
                # It is safe to use the most frequent character.
                result += char

                # We used one copy.
                count += 1

            # Put the first character back if copies remain.
            if count != 0:
                heapq.heappush(max_heap, (count, char))

        return result